from MemoryManager import MemoryManager
from Stack import Stack
from SymbolTable import IdInfo, SymbolTable
from TransitionDiagram import Routine
import constants as cs


class CodeGenerator:
    def __init__(self, symbol_table: SymbolTable):
        self.symbol_table = symbol_table
        self.memory_manager = MemoryManager(start_index=500)
        self.program_block = [("", "", "", "")]
        self.current_line = 1
        self.ss = Stack()
        self.last_declared_func = None
        self.break_stack = Stack()
        self.while_starts = Stack()
        self.nested_func_stack = Stack()
        self.end_of_current_func = None

    def call_routines_list(self, routines: list, current_token: IdInfo):
        for routine in routines:
            self.call_routine(routine, current_token)

    def call_routine(self, routine: Routine, current_token=None):
        print("#", routine.name)
        print("line : ",self.current_line)
        eval("self.{}(current_token)".format(routine.name))
        self.ss.prin()

    ####################  routines  ####################

    def set_main_address(self, main_address: int):
        self.program_block[0] = ("JP",
                                 str(main_address),
                                 "",
                                 "")

    def get_temp(self):
        tmp_var = IdInfo("tmp", type="int", size=4, addressing_mode=cs.DIRECT)
        tmp_var.address = self.memory_manager.get_temp(tmp_var)
        return tmp_var

    def push_constant(self, current_token: IdInfo):
        current_token.addressing_mode = cs.IMMEDIATE
        current_token.type = cs.INT
        self.ss.push(current_token)

    def assign_and_keep(self, current_token: IdInfo):
        self.program_block.append(("ASSIGN",
                                   self.ss.list[-1].address_in_program(),
                                   self.ss.list[-2].address_in_program(),
                                   ""))
        self.current_line += 1
        self.ss.pop(1)

    def pop(self, current_token: IdInfo):
        self.ss.pop(1)

    def p_type(self, current_token: IdInfo):
        if current_token.token not in [cs.INT, cs.VOID]:
            print("Error: type is unknown")
        current_token.type = cs.TYPE
        self.ss.push(current_token)

    def p_id(self, current_token: IdInfo):
        # print(current_token.__str__())
        id_info = self.symbol_table.find(current_token.token)
        self.ss.push(id_info)

    def push_function_id(self, current_token: IdInfo):
        func_id_info = self.symbol_table.find(current_token.token)
        self.last_declared_func = func_id_info
        func_id_info.type = self.ss.list[-1].token
        func_id_info.size = 4
        func_id_info.is_function = True
        self.ss.pop(1)
        self.ss.push(func_id_info)

    def save_fun_line_address_and_save_line(self, current_token: IdInfo):
        var_end_of_func = self.get_temp()
        var_end_of_func.addressing_mode = cs.INDIRECT
        var_end_of_func.line = self.current_line
        self.nested_func_stack.push(var_end_of_func)
        self.program_block.append((0, 0, 0, 0))
        self.current_line += 1

        func_id_info = self.ss.top()
        func_id_info.size += 8  # for return line address and return line and start line
        func_id_info.address = self.memory_manager.get_temp(func_id_info)
        func_id_info.addressing_mode = cs.DIRECT
        func_id_info.params_count = 0

        line_num = IdInfo(str(self.current_line), type=cs.INT, addressing_mode=cs.IMMEDIATE)
        self.ss.pop(1)
        self.ss.push(line_num)
        self.program_block.append((0, 0, 0, 0))
        self.current_line += 1
        func_id_info.starting_line = self.current_line
        if func_id_info.token == "main":
            self.set_main_address(func_id_info.starting_line)
        self.ss.push(func_id_info)

    def declare_zero_params_func(self, current_token: IdInfo):
        func_id_info = self.ss.list[-1]
        func_id_info.params_count = 0

    def declare_param_int(self, current_token: IdInfo):
        self.ss.list[-1].is_array = False
        self.ss.list[-1].addressing_mode = cs.DIRECT

    def declare_param_arr(self, current_token: IdInfo):
        self.ss.list[-1].is_array = True
        self.ss.list[-1].addressing_mode = cs.INDIRECT

    def push_param_in_func(self, current_token: IdInfo):
        tmp_param_id_info = self.ss.list[-1]
        tmp_param_id_info.type = self.ss.list[-2].token
        tmp_param_id_info.size = 4
        tmp_param_id_info.address = self.memory_manager.get_temp(self.ss.list[-1])
        tmp_func_id_info = self.ss.list[-3]
        tmp_func_id_info.params_count += 1
        print(tmp_param_id_info.address_in_program(),tmp_param_id_info.addressing_mode)
        self.ss.pop(2)

    def set_return_value(self, current_token: IdInfo):
        self.program_block.append(("ASSIGN",
                                   self.ss.list[-1].address_in_program(),
                                   self.ss.list[-2].address_in_program(),
                                   ""))
        self.current_line += 1
        self.ss.pop(1)

    def jp_to_caller(self, current_token: IdInfo):
        self.program_block.append(("JP",
                                   str(self.nested_func_stack.top().address_in_program()),
                                   "",
                                   ""))
        self.current_line += 1

    def jp_to_caller_final(self, current_token: IdInfo):
        current_func = self.nested_func_stack.top()
        self.program_block[current_func.line] = ("ASSIGN",
                                                             "#"+str(self.current_line),
                                                             str(current_func.address),
                                                             "")
        self.nested_func_stack.pop(1)
        self.program_block.append(("JP",
                                   "@" + str(self.ss.list[-1].address + 4),
                                   "",
                                   ""))
        self.current_line += 1
        self.ss.pop(1)
        self.program_block[int(self.ss.top().token)] = (("JP",
                                                         str(self.current_line),
                                                         "",
                                                         ""))
        self.ss.pop(1)

    def p_func_id(self, current_token: IdInfo):
        func_id_info = self.symbol_table.find(current_token.token)
        func_id_info.current_param = 0
        self.ss.push(func_id_info)

    def put_arg(self, current_token: IdInfo):
        arg_id_info = self.ss.list[-1]
        func_id_info = self.ss.list[-2]
        self.program_block.append(("ASSIGN",
                                   str(arg_id_info.address_for_func()),
                                   str(func_id_info.address + 12 + 4 * func_id_info.current_param),
                                   ""))
        self.current_line += 1
        func_id_info.current_param += 1
        self.ss.pop(1)

    def set_return_line(self, current_token: IdInfo):
        func_id_info = self.ss.list[-1]
        self.program_block.append(("ASSIGN",
                                   "#" + str(self.current_line+3),
                                   str(func_id_info.address + 4),
                                   ""))
        self.current_line += 1

    def call_func(self, current_token: IdInfo):
        func_id_info = self.ss.list[-1]
        self.program_block.append(("JP",
                                   str(func_id_info.starting_line),
                                   "",
                                   ""))
        self.current_line += 1

    def mult(self, current_token):
        tmp_var = self.get_temp()
        self.program_block.append(("MULT",
                                   self.ss.list[-1].address_in_program(),
                                   self.ss.list[-2].address_in_program(),
                                   tmp_var.address_in_program()))
        self.current_line += 1
        self.ss.pop(2)
        self.ss.push(tmp_var)

    def p_operation(self, current_token: IdInfo):
        if (current_token.token not in cs.operators) or (current_token.type != cs.OPERATION):
            print("Invalid Operation")
            return
        self.ss.push(current_token)

    def operate(self, current_token):
        tmp_var = self.get_temp()
        operator_token = self.ss.list[-2].token
        operation = ""
        if operator_token == "+":
            operation = "ADD"
        elif operator_token == "-":
            operation = "SUB"
        elif operator_token == "<":
            operation = "LT"
        elif operator_token == "==":
            operation = "EQ"
        else:
            print("Parse Error: Unknown Operator")
        self.program_block.append((operation,
                                   self.ss.list[-3].address_in_program(),
                                   self.ss.list[-1].address_in_program(),
                                   tmp_var.address_in_program()))
        self.current_line += 1
        self.ss.pop(3)
        self.ss.push(tmp_var)

    def p_arr_value(self, current_token: IdInfo):
        relative_arr_pointer = self.get_temp()
        self.program_block.append(("MULT",
                                   self.ss.list[-1].address_in_program(),
                                   "#" + str(self.ss.list[-2].size),
                                   relative_arr_pointer.address_in_program()))
        actual_arr_pointer = self.get_temp()
        self.program_block.append(("ADD",
                                   self.ss.list[-2].address_in_program(),
                                   relative_arr_pointer.address_in_program(),
                                   actual_arr_pointer.address_in_program()))
        self.current_line += 2
        self.ss.pop(2)
        self.ss.push(actual_arr_pointer)

    def start_declaration(self, current_token):
        self.symbol_table.declaration_usage_not = True

    def end_declaration(self, current_token):
        self.symbol_table.declaration_usage_not = False

    def declare_int(self, current_token):
        if self.ss.list[-2].token != cs.INT:
            print("Error: cannot declare variable of non-int type")
            return
        self.ss.list[-1].type = cs.INT
        self.ss.list[-1].size = 4
        self.ss.list[-1].address = self.memory_manager.get_temp(self.ss.list[-1])
        self.ss.list[-1].is_array = False
        self.ss.list[-1].addressing_mode = cs.DIRECT
        self.ss.pop(2)

    def declare_arr(self, current_token):
        if self.ss.list[-3].token != cs.INT:
            print("Error: cannot declare array of non-int type")
            return
        self.ss.list[-2].type = cs.INT
        self.ss.list[-2].size = int(self.ss.list[-1].token) * 4
        self.ss.list[-2].is_array = True
        self.ss.list[-2].array_size = int(self.ss.list[-1].token) * 4
        self.ss.list[-2].address = self.memory_manager.get_temp(self.ss.list[-2])
        self.ss.list[-2].addressing_mode = cs.DIRECT
        self.ss.pop(3)

    def new_scope(self, current_token: IdInfo):
        self.symbol_table.new_scope()

    def delete_scope(self, current_token: IdInfo):
        self.symbol_table.delete_scope()

    def save_line(self, current_token: IdInfo):
        line_num = IdInfo(str(self.current_line), type=cs.INT, addressing_mode=cs.IMMEDIATE)
        self.ss.push(line_num)
        self.program_block.append((0, 0, 0, 0))
        self.current_line += 1

    def write_jpf(self, current_token: IdInfo):
        self.program_block[int(self.ss.list[-2].token)] = ("JPF",
                                                           self.ss.list[-3].address_in_program(),
                                                           str(self.current_line),
                                                           "")

    def write_jp(self, current_token: IdInfo):
        self.program_block[int(self.ss.list[-1].token)] = ("JP",
                                                           self.current_line,
                                                           "",
                                                           "")
        self.ss.pop(3)

    def push_break_stack(self, current_token: IdInfo):
        var_end_of_while = self.get_temp()
        var_end_of_while.addressing_mode = cs.INDIRECT
        var_end_of_while.line = self.current_line
        self.break_stack.push(var_end_of_while)
        self.program_block.append((0, 0, 0, 0))
        self.current_line += 1

    def push_continue_stack(self, current_token: IdInfo):
        line_num = IdInfo(str(self.current_line), type=cs.INT, addressing_mode=cs.IMMEDIATE)
        self.while_starts.push(line_num)

    def jpf_to_break(self, current_token: IdInfo):
        self.program_block.append(("JPF",
                                   self.ss.list[-1].address_in_program(),
                                   self.break_stack.list[-1].address_in_program(),
                                   ""))
        self.current_line += 1
        self.ss.pop(1)

    def jp_continue_address(self, current_token: IdInfo):
        self.program_block.append(("JP",
                                   self.while_starts.list[-1].token,
                                   "",
                                   ""))
        self.current_line += 1

    def set_top_break_value(self, current_token: IdInfo):
        # self.break_stack.list[-1]
        self.program_block[self.break_stack.list[-1].line] = ("ASSIGN",
                                                                     "#" + str(self.current_line),
                                                                     str(self.break_stack.list[-1].address),
                                                                     "")

    def pop_break_top(self, current_token: IdInfo):
        self.break_stack.pop(1)

    def pop_continue(self, current_token: IdInfo):
        self.while_starts.pop(1)

    def jp_to_break(self, current_token: IdInfo):
        self.program_block.append(("JP",
                                   self.break_stack.list[-1].address_in_program(),
                                   "",
                                   ""))
        self.current_line += 1

    def compare_save_for_jpf(self, current_token: IdInfo):
        tmp_var = self.get_temp()
        self.program_block.append(("EQ",
                                   self.ss.list[-1].address_in_program(),
                                   self.ss.list[-2].address_in_program(),
                                   tmp_var.address_in_program()))
        self.current_line += 1
        self.ss.pop()
        self.ss.push(tmp_var)
        line_num = IdInfo(str(self.current_line), type=cs.INT, addressing_mode=cs.IMMEDIATE)
        self.ss.push(line_num)
        self.program_block.append((0, 0, 0, 0))
        self.current_line += 1

    def jpf_set_for_case(self, current_token: IdInfo):
        self.program_block[int(self.ss.list[-1].token)] = ("JPF",
                                                           self.ss.list[-2].address_in_program(),
                                                           str(self.current_line),
                                                           "")
        self.ss.pop(2)

    #############    SEMANTIC   #############

    def assert_func_void(self, current_token: IdInfo):
        if self.last_declared_func.type != cs.VOID:
            print("Error : function {} must return value".format(self.ss.list[-1].token))

    def assert_func_int(self, current_token: IdInfo):
        if self.ss.list[-1].type != cs.INT:
            print("Error : function {} cannot return value".format(self.ss.list[-1].token))

    def assert_in_while(self, current_token: IdInfo):
        if len(self.break_stack.list) == 0:
            print("Error: break and continue must be used in while")

    def assert_type_int(self, current_token: IdInfo):
        id_info = self.ss.list[-1]
        if id_info.address == None:
            print("Error: variable {} has not been declared".format(id_info.token))
        elif id_info.type != "int":
            print("Error: variable {} is declared as int".format(id_info.token))

    def assert_arr(self, current_token: IdInfo):
        id_info = self.ss.list[-1]
        if id_info.address == None:
            print("Error: variable {} has not been declared yet".format(id_info.token))
        if id_info.type != "int":
            print("Error: array {} is declared for ints".format(id_info.token))
        if not id_info.is_array:
            print("Error: variable {} is declared as an array".format(id_info.token))
        # elif id_info.array_size is None:
        #     print("Error: array {} does not have a size".format(id_info.token))

    def assert_index(self, current_token: IdInfo):
        pass
        # index_info = self.ss.list[-1]
        # array_info = self.ss.list[-2]
        # if index_info.type != "int":
        #     print("Error: array index must be of type int")
        # if index_info.addressing_mode == cs.IMMEDIATE:
        #     if int(index_info.token) >= array_info.array_size or int(index_info.token) < 0:
        #         print("Error: array index out of bounds {}".format(array_info.array_size))

    def assert_type_check(self, current_token):
        var1 = self.ss.list[-1]
        var2 = self.ss.list[-2]
        if var1.type != var2.type:
            print("error at line {}:\nMult term types dont match!".format(self.current_line))
        if var1.type != "int" or var2.type != "int":
            print("error at line {}:\nMult term type must be int!".format(self.current_line))

    def assert_operation_type(self, current_token):
        var1 = self.ss.list[-1]
        var2 = self.ss.list[-3]
        if var1.type != var2.type:
            print("error at line {}:\nMult term types dont match!".format(self.current_line))
        if var1.type != "int" or var2.type != "int":
            print("error at line {}:\nMult term type must be int!".format(self.current_line))

    def assert_args_count(self, current_id: IdInfo):
        func_id_info = self.ss.list[-1]
        print(func_id_info.params_count, func_id_info.current_param)
        if func_id_info.params_count != func_id_info.current_param:
            print("Error: wrong number of inputs for function {}".format(func_id_info.token))
        func_id_info.current_param = 0

    def assert_repetition(self, current_id: IdInfo):
        # for functions
        pass

    def assert_arg_type(self, current_id: IdInfo):
        pass

    def main_check(self, current_id: IdInfo):
        if (self.last_declared_func.token != "main") or (self.last_declared_func.params_count != 0) or (
                self.last_declared_func.type != cs.VOID):
            print("Error: program's main function isn't declared correctly")

    def output_func_declare(self, current_id: IdInfo):
        # type - specifier ID  # push_function_id #new_scope ( #save_fun_line_address_and_save_line params ) compound-stmt #delete_scope",  ###
        type_info = IdInfo("void", type=cs.TYPE)
        self.ss.push(type_info)
        func_id_info = IdInfo("output")
        self.push_function_id(func_id_info)
        self.new_scope(current_id)
        self.save_fun_line_address_and_save_line(current_id)
        param_type_info = IdInfo("int", type=cs.TYPE)
        self.ss.push(param_type_info)
        param_info = IdInfo("s")
        self.ss.push(param_info)
        self.declare_param_int(current_id)
        self.push_param_in_func(current_id)
        s = self.symbol_table.find("s")
        self.program_block.append(("PRINT",
                                   s.address_in_program(),
                                   "",
                                   ""))
        self.current_line += 1
        # self.jp_to_caller(current_id)
        self.jp_to_caller_final(current_id)
        self.delete_scope(current_id)
