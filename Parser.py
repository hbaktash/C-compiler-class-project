import sys
import time

from CodeGenerator import CodeGenerator
from Stack import Stack
from SymbolTable import IdInfo, SymbolTable
from TransitionDiagram import State, TransitionDiagram, Routine
from Scanner import Scanner

STATE = 0
PRE_ROUTINES = 1
POST_ROUTINES = 2
IS_EPSILON = 3


class Parser:
    def __init__(self, input_code: str):  # TODO initialize
        self.symbol_table = SymbolTable()
        self.symbol_table.new_scope()
        self.pars_stack = Stack()
        self.scanner = Scanner(input_code, symbol_table=self.symbol_table)
        self.dfa = TransitionDiagram()  # TODO
        self.dfa.make_diagrams()
        self.look_ahead = ""
        self.current_token = None
        self.current_token_info = None
        self.pars_stack.push(self.dfa.start_state)
        self.code_generator = CodeGenerator(self.symbol_table)

    def run(self):
        token_info, self.look_ahead = self.scanner.look_ahead()
        ignored_string = ""
        while True:
            # print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            top = self.pars_stack.top()
            # print("         Top : ", top.type, " ", top.name, " Look ahead=",self.look_ahead)
            if top.type == "state":
                state = top
                if state.is_final:
                    # print("         poped", top.name)
                    self.pars_stack.pop()
                    if state.is_omega_final:
                        print("Parsed successfully!")
                        break
                elif not state.is_final:
                    if self.look_ahead in state.goto_dict:  # key exists in dict
                        ignored_string = ""
                        pre_routines = Routine.string_to_routines(state.goto_dict[self.look_ahead][PRE_ROUTINES])
                        post_routines = Routine.string_to_routines(state.goto_dict[self.look_ahead][POST_ROUTINES])
                        self.code_generator.call_routines_list(pre_routines, self.current_token_info)
                        next_state = state.goto_dict[self.look_ahead][STATE]
                        if len(next_state) == 1:  # if edge is terminal
                            next_state = next_state[0]
                            # print("on a terminal edge")
                            # print("         poped ", self.pars_stack.top().name)
                            self.pars_stack.pop()
                            self.current_token = self.look_ahead
                            self.current_token_info = token_info
                            self.code_generator.call_routines_list(post_routines, current_token=self.current_token_info)
                            self.pars_stack.push(next_state)
                            # print("         pushed ", next_state.type, " ", next_state.name)
                            if not state.goto_dict[self.look_ahead][IS_EPSILON]:
                                token_info, self.look_ahead = self.scanner.look_ahead()
                        elif len(next_state) == 2:
                            # print("on a non-terminal edge")
                            # print("         poped ", self.pars_stack.top().name)
                            self.pars_stack.pop()
                            # print("         pushed ", next_state[1].name)
                            self.pars_stack.push(
                                next_state[1])  # next state in this diagram (not the nonterminal's diagram)
                            for routine in reversed(post_routines):
                                self.pars_stack.push(routine)
                            # print("         pushed ", next_state[0].name)
                            self.pars_stack.push(next_state[0])  # start state of the nonterminal
                        else:
                            print("ERROR in initializing states: next state with 0 or >2 elements")
                    else:  # key doesnt exist in dict
                        ignored_string += self.look_ahead
                        token_info, self.look_ahead = self.scanner.look_ahead()
                        if self.look_ahead == "$":
                            print("Error: reached end of file.")
                            break
                        print("Error in line:\n  Panic Mode: Error in input, ignored: ", ignored_string)
                        continue
                else:
                    print("!!?")
            elif top.type == "#":
                self.code_generator.call_routine(top, current_token=self.current_token_info)
                self.pars_stack.pop()


code = "int var1;" \
       "int function1(int a){" \
       "    void function2(int b, int c){" \
       "        if(c < 2)" \
       "        output(b);" \
       "        else;" \
       "        output(a);  " \
       "    }" \
       "    int d;" \
       "    int function3(void){" \
       "        int c;" \
       "        c = 0;" \
       "        switch(var1){" \
       "            case 1:" \
       "                c = a;" \
       "                break;" \
       "            case 2:" \
       "                c = a-2;" \
       "            case 3:" \
       "                c = c + 1;" \
       "                break;" \
       "            default: c=9;" \
       "        }" \
       "        return c;" \
       "    }" \
       "    d = 4;" \
       "    var1 = 2;" \
       "    function2(function3(),d);" \
       "    return 1;" \
       "}" \
       "int array1[5];" \
       "void main(void){" \
       "int i;" \
       "i = 5;" \
       "if(function1(i)) return;" \
       "else ;" \
       "while(i){" \
       "array1[i = i - 1] = i;" \
       "-37;" \
       "output(array1[i]);" \
       "}" \
       "}" \
       "EOF"

code = "int f(int a){" \
       "    return a+1;" \
       "}" \
       "void main(void){" \
       "    f(2);" \
       "} " \
       "EOF"
parser = Parser(code)
parser.run()
i = 0
with open("./Tester/output.txt",mode='w') as f:
    for line in parser.code_generator.program_block:
        str_tmp = str(i)+"\t("+str(line[0])+","+str(line[1])+","+str(line[2])+","+str(line[3])+")\n"
        i += 1
        f.write(str_tmp)
        print(str_tmp,end='')
