import constants as cs


class State:
    def __init__(self, name="S0", is_final=False, is_omega_final = False):
        self.goto_dict = {}  # { terminal : [ [next States] ,[pre routines], [post routines], is_epsilon]
        self.is_final = is_final
        self.is_omega_final = is_omega_final
        self.name = name
        self.type = "state"  # #a#B#c


class Routine:
    def __init__(self, is_semantic, name="default"):
        self.name = name
        self.is_semantic = is_semantic
        self.type = "#"

    @staticmethod
    def string_to_routines(routines_str: list):
        if len(routines_str) != 0:
            routines = [Routine(False, name=string) for string in (" "+routines_str[0]).split(" #")]
            routines = routines[1:]
        else:
            routines = []
        return routines


class TransitionDiagram:
    def __init__(self):
        self.start_state = None
        self.current_state = None
        self.finish_states = None
        self.states = None

        self.declaration_states = []
        self.declaration_list_states = []
        self.program_states = []
        self.compound_stmt_states = []
        self.additive_expression_states = []
        self.term_states = []
        self.additive_expression_extension_states = []
        self.term_extension_states = []
        self.relop_states = []
        self.var_extension_states = []
        self.var_states = []
        self.expression_states = []
        self.expression_stmt_states = []
        self.selection_stmt_states = []
        self.iteration_stmt_states = []
        self.return_stmt_states = []
        self.case_stmt_states = []
        self.switch_stmt_states = []
        self.default_stmt_states = []
        self.var_states = []
        self.args_states = []
        self.call_states = []
        self.simple_expression_states = []
        self.factor_states = []
        self.addop_states = []
        self.additive_expression_states = []
        self.factor_states = []
        self.statement_state = []
        self.param_list_state = []
        self.params_state = []
        self.param_extension_state = []
        self.param_state = []
        self.arg_list_states = []

    def make_diagrams(self):

        # ------- transition diagrams
        for i in range(4):
            self.arg_list_states.append(State(name=("arg_list_{}".format(i))))
        for i in range(10):
            self.declaration_states.append(State(name= ("declaration_{}".format(i))))
        for i in range(3):
            self.declaration_list_states.append(State(name= ("declaration_list_{}".format(i))))
        for i in range(3):
            self.program_states.append(State(name= ("program_{}".format(i))))
        for i in range(5):
            self.compound_stmt_states.append(State(name= ("compound_stmt_{}".format(i))))
        for i in range(4):
            self.additive_expression_states.append(State(name= ("additive_expression_{}".format(i))))
        for i in range(3):
            self.term_states.append(State(name= ("term_{}".format(i))))
        for i in range(3):
            self.additive_expression_extension_states.append(State(name= ("additive_expression_extension_stmt_{}".format(i))))
        for i in range(3):
            self.term_extension_states.append(State(name= ("term_extension_{}".format(i))))
        for i in range(2):
            self.relop_states.append(State(name= ("relop_{}".format(i))))
        for i in range(4):
            self.var_extension_states.append(State(name=("var_extension_{}".format(i))))
        for i in range(3):
            self.var_states.append(State(name=("var_{}".format(i))))
        for i in range(14):
            self.expression_states.append(State(name= ("expression_{}".format(i))))
        for i in range(3):
            self.expression_stmt_states.append(State(name= ("expression_stmt_{}".format(i))))
        for i in range(8):
            self.selection_stmt_states.append(State(name= ("selection_stmt_{}".format(i))))
        for i in range(6):
            self.iteration_stmt_states.append(State(name= ("iteration_stmt_{}".format(i))))
        for i in range(4):
            self.return_stmt_states.append(State(name= ("return_stmt_{}".format(i))))
        for i in range(5):
            self.case_stmt_states.append(State(name= ("case_stmt_{}".format(i))))
        for i in range(8):
            self.switch_stmt_states.append(State(name= ("switch_stmt_{}".format(i))))
        for i in range(4):
            self.default_stmt_states.append(State(name= ("default_stmt_{}".format(i))))
        for i in range(5):
            self.var_states.append(State(name= ("var_{}".format(i))))
        for i in range(4):
            self.args_states.append(State(name= ("args_{}".format(i))))
        for i in range(5):
            self.call_states.append(State(name= ("call_{}".format(i))))
        for i in range(4):
            self.simple_expression_states.append(State(name= ("simple_expression_{}".format(i))))
        for i in range(2):
            self.factor_states.append(State(name= ("factor_{}".format(i))))
        for i in range(2):
            self.addop_states.append(State(name= ("addop_{}".format(i))))
        for i in range(4):
            self.additive_expression_states.append(State(name= ("additive_expression_{}".format(i))))
        for i in range(7):
            self.factor_states.append(State(name=("factor_{}".format(i))))
        for i in range(2):
            self.statement_state.append(State(name=("statement_{}".format(i))))
        for i in range(4):
            self.param_list_state.append(State(name=("param_list_{}".format(i))))
        for i in range(7):
            self.params_state.append(State(name=("params_{}".format(i))))
        for i in range(3):
            self.param_extension_state.append(State(name=("param_extension_{}".format(i))))
        for i in range(4):
            self.param_state.append(State(name=("param_{}".format(i))))

        arg_list_states = self.arg_list_states
        declaration_states = self.declaration_states
        declaration_list_states = self.declaration_list_states
        program_states = self.program_states
        compound_stmt_states = self.compound_stmt_states
        term_states = self.term_states
        additive_expression_extension_states = self.additive_expression_extension_states
        term_extension_states = self.term_extension_states
        relop_states = self.relop_states
        var_extension_states = self.var_extension_states
        expression_states = self.expression_states
        expression_stmt_states = self.expression_stmt_states
        selection_stmt_states = self.selection_stmt_states
        iteration_stmt_states = self.iteration_stmt_states
        return_stmt_states = self.return_stmt_states
        case_stmt_states = self.case_stmt_states
        switch_stmt_states = self.switch_stmt_states
        default_stmt_states = self.default_stmt_states
        var_states = self.var_states
        args_states = self.args_states
        addop_states = self.addop_states
        additive_expression_states = self.additive_expression_states
        factor_states = self.factor_states
        statement_state = self.statement_state
        param_list_state = self.param_list_state
        params_state = self.params_state
        param_extension_state = self.param_extension_state
        param_state = self.param_state


        # -------- param-extension

        # -------- arg-list
        for first in cs.First["expression"]:
            arg_list_states[0].goto_dict[first] = [[expression_states[0], arg_list_states[1]], [] , ["#assert_arg_type #put_arg"], False]
        arg_list_states[1].goto_dict[","] = [[arg_list_states[2]],[],[],False]
        for follow in cs.Follow["arg-list"]:
            arg_list_states[1].goto_dict[follow] = [[arg_list_states[3]],[],[],True]
        for first in cs.First["arg-list"]:
            arg_list_states[2].goto_dict[first] = [[arg_list_states[0], arg_list_states[3]],[],[],False]
        arg_list_states[3].is_final = True
        # -------- args
        for first in cs.First["expression"]:
            args_states[0].goto_dict[first] = [[expression_states[0], args_states[1]], [] , ["#assert_arg_type #put_arg"], False]
        for follow in cs.Follow["args"]:
            args_states[0].goto_dict[follow] = [[args_states[3]], [], [], True]
        args_states[1].goto_dict[","] = [[args_states[2]],[],[],False]
        for follow in cs.Follow["args"]:
            args_states[1].goto_dict[follow] = [[args_states[3]],[],[],True]
        for first in cs.First["arg-list"]:
            args_states[2].goto_dict[first] = [[arg_list_states[0], args_states[3]],[],[],False]
        args_states[3].is_final = True

        # ------- factor
        factor_states[0].goto_dict["("] = [[factor_states[1]], [], [],False]
        factor_states[0].goto_dict["NUM"] = [[factor_states[6]], [], ["#push_constant"],False]
        factor_states[0].goto_dict["ID"] = [[factor_states[3]], [], [],False]

        for first in cs.First["expression"]:
            factor_states[1].goto_dict[first] = [[expression_states[0], factor_states[2]], [], [],False]

        factor_states[2].goto_dict[")"] = [[factor_states[6]], [], [],False]

        factor_states[3].goto_dict["("] = [[factor_states[4]], ["#p_func_id"], [],False]

        for first in cs.First["var-extension"]:
            factor_states[3].goto_dict[first] = [[var_extension_states[0], factor_states[6]], ["#p_id"], [],False]
        for follow in cs.Follow["var-extension"]:
            factor_states[3].goto_dict[follow] = [[ factor_states[6]], ["#p_id"], ["#assert_type_int"],True]

        for first in cs.First["args"]:
            factor_states[4].goto_dict[first] = [[args_states[0], factor_states[5]], [], ["#set_return_line #assert_args_count #call_func"],False]
        for follow in cs.Follow["args"]:
            factor_states[4].goto_dict[follow] = [[factor_states[5]], [], ["#set_return_line #assert_args_count #call_func"], True]

        factor_states[5].goto_dict[")"] = [[factor_states[6]], [], [],False]

        factor_states[6].is_final = True


        #-------- declaration

        declaration_states[0].goto_dict["int"] = [[declaration_states[1]], ["#start_declaration"], ["#p_type"], False]
        declaration_states[0].goto_dict["void"] = [[declaration_states[1]], ["#start_declaration"], ["#p_type"], False]
        declaration_states[1].goto_dict["ID"] = [[declaration_states[2]], [], [], False]
        declaration_states[2].goto_dict[";"] = [[declaration_states[9]], ["#p_id"], ["#declare_int #end_declaration"],False]
        declaration_states[2].goto_dict["["] = [[declaration_states[3]], ["#p_id"], [], False]
        declaration_states[2].goto_dict["("] = [[declaration_states[6]], [" #push_function_id"], ["#new_scope #save_fun_line_address_and_save_line"], False]
        declaration_states[3].goto_dict["NUM"] = [[declaration_states[4]], [], ["#push_constant"],False]
        declaration_states[4].goto_dict["]"] = [[declaration_states[5]], [], [],False]
        declaration_states[5].goto_dict[";"] = [[declaration_states[9]], ["#declare_arr"], ["#end_declaration"],False]
        for first in cs.First["params"]:
            declaration_states[6].goto_dict[first] = [[params_state[0],declaration_states[7]], [], [],False]
        declaration_states[7].goto_dict[")"] = [[declaration_states[8]], ["#end_declaration"], [],False]
        for first in cs.First["coumpound-stmt"]:
            declaration_states[8].goto_dict[first] = [[compound_stmt_states[0],declaration_states[9]], [], ["#jp_to_caller_final #delete_scope"],False]
        declaration_states[9].is_final = True


        # ------- decalration list

        for first in cs.First["declaration"]:
            declaration_list_states[0].goto_dict[first] = [[declaration_states[0], declaration_list_states[0]], [], [], False]

        for follow in cs.Follow["declaration-list"]:
            declaration_list_states[0].goto_dict[follow] = [[declaration_list_states[1]], [], [], True]

        declaration_list_states[1].is_final = True



        #--------- program

        self.start_state = program_states[0]
        for first in cs.First["declaration-list"]:
            program_states[0].goto_dict[first] = [[declaration_list_states[0], program_states[1]], ["#new_scope #output_func_declare"], [], False]
        for follow in cs.Follow["declaration-list"]:
            program_states[0].goto_dict[follow] = [[program_states[1]], [], [], True]

        program_states[1].goto_dict["EOF"] = [[program_states[2]], [], ["#main_check #delete_scope"], False]

        program_states[2].is_omega_final = True
        program_states[2].is_final = True


        #------- compound stmt

        compound_stmt_states[0].goto_dict["{"] = [[compound_stmt_states[1]], ["#new_scope"], [], False]
        for first in cs.First["declaration-list"]:
            compound_stmt_states[1].goto_dict[first] = [[declaration_list_states[0], compound_stmt_states[2]], [], [], False]
        for follow in cs.Follow["declaration-list"]:
            compound_stmt_states[1].goto_dict[follow] = [[compound_stmt_states[2]], [], [], True]
        for first in cs.First["statement"]:
            compound_stmt_states[2].goto_dict[first] = [[statement_state[0], compound_stmt_states[2]], [], [], False]
        # for follow in cs.Follow["statement-list"]:
        #     compound_stmt_states[2].goto_dict[follow] = [[compound_stmt_states[3]], [], [], True]
        compound_stmt_states[2].goto_dict["}"] = [[compound_stmt_states[3]], ["#delete_scope"], [], False]
        compound_stmt_states[3].is_final = True

        # ------- additive expression

        for first in cs.First["term"]:
            additive_expression_states[0].goto_dict[first] = [[term_states[0], additive_expression_states[1]], [], [],False]

        for first in cs.First["addop"]:
            additive_expression_states[1].goto_dict[first] = [[addop_states[0], additive_expression_states[2]], [], [],False]

        for follow in cs.Follow["additive-expression"]:
            additive_expression_states[1].goto_dict[follow] = [[additive_expression_states[3]], [], [], True]

        for first in cs.First["additive-expression"]:
            additive_expression_states[2].goto_dict[first] = [[additive_expression_states[0], additive_expression_states[3]], [], ["#assert_operation_type #operate"],False]

        additive_expression_states[3].is_final = True


        #------- additive expression extension

        for first in cs.First["addop"]:
            additive_expression_extension_states[0].goto_dict[first] = [[addop_states[0], additive_expression_extension_states[1]], [], [],False]

        for follow in cs.Follow["additive-expression-extension"]:
            additive_expression_states[0].goto_dict[follow] = [[additive_expression_states[2]], [], [], True]

        for first in cs.First["additive-expression"]:
            additive_expression_extension_states[1].goto_dict[first] = [[additive_expression_states[0], additive_expression_extension_states[2]], [], ["#assert_operation_type #operate"],False]

        additive_expression_extension_states[2].is_final = True

        # ------- term

        for first in cs.First["factor"]:
            term_states[0].goto_dict[first] = [[factor_states[0],term_states[1]], [], [],False]

        for first in cs.First["term-extension"]:
            term_states[1].goto_dict[first] = [[term_extension_states[0], term_states[2]], [], [],False]
        for follow in cs.Follow["term-extension"]:
            term_states[1].goto_dict[follow] = [[term_states[2]], [], [], True]

        term_states[2].is_final = True

        # ------- term extension

        term_extension_states[0].goto_dict["*"] = [[term_extension_states[1]], [], [],False]

        for first in cs.First["term"]:
            term_extension_states[1].goto_dict[first] = [[term_states[0], term_extension_states[2]], [], ["#assert_type_check #mult"],False]
        for follow in cs.Follow["term-extension"]:
            term_extension_states[1].goto_dict[follow] = [[term_extension_states[2]], [], [], True]

        term_extension_states[2].is_final = True

        # ------- relop

        relop_states[0].goto_dict["<"] = [[relop_states[1]], [], ["#p_operation"],False]
        relop_states[0].goto_dict["=="] = [[relop_states[1]], [], ["#p_operation"],False]

        relop_states[1].is_final = True

        # ------ addop

        addop_states[0].goto_dict["+"] = [[addop_states[1]], [], ["#p_operation"],False]
        addop_states[0].goto_dict["-"] = [[addop_states[1]], [], ["#p_operation"],False]
        addop_states[1].is_final = True

        # ------ var extension

        var_extension_states[0].goto_dict["["] = [[var_extension_states[1]], ["#assert_arr"], [],False]

        for first in cs.First["expression"]:
            var_extension_states[1].goto_dict[first] = [[expression_states[0], var_extension_states[2]], [], [],False]
        var_extension_states[2].goto_dict["]"] = [[var_extension_states[3]], ["#assert_index"], ["#p_arr_value"], False]
        var_extension_states[3].is_final = True

        # ------ var

        var_states[0].goto_dict["ID"] = [[var_states[1]], [], ["#p_id"], False]

        for first in cs.First["var-extension"]:
            var_states[1].goto_dict[first] = [[var_extension_states[0], var_states[2]], [], [],False]
        for follow in cs.Follow["var-extension"]:
            var_states[1].goto_dict[follow] = [[var_states[2]], [], ["#assert_type_int"],True]

        var_states[1].is_final = True

        # ------ expression

        expression_states[0].goto_dict["ID"] = [[expression_states[1]], [], [],False]
        expression_states[0].goto_dict["NUM"] = [[expression_states[9]], [], ["#push_constant"],False]
        expression_states[0].goto_dict["("] = [[expression_states[2]], [], [],False]


        for first in cs.First["var-extension"]:
            expression_states[1].goto_dict[first] = [[var_extension_states[0], expression_states[3]], ["#p_id"], [],False]
        for follow in cs.Follow["var-extension"]:
            expression_states[1].goto_dict[follow] = [[expression_states[3]], ["#p_id"], ["#assert_type_int"],True]
        expression_states[1].goto_dict["("] = [[expression_states[4]], ["#p_func_id"], [],False]

        for first in cs.First["expression"]:
            expression_states[2].goto_dict[first] = [[expression_states[0], expression_states[7]], [], [],False]


        expression_states[3].goto_dict["="] = [[expression_states[8]], [], [],False]
        expression_states[3].goto_dict["*"] = [[expression_states[5]], [], [],False]
        for first in cs.First["additive-expression-extension"]:
            expression_states[3].goto_dict[first] = [[additive_expression_extension_states[0], expression_states[11]], [], [],False]
        for follow in cs.Follow["additive-expression-extension"]:
            expression_states[3].goto_dict[follow] = [[expression_states[11]], [], [],True]

        for first in cs.First["args"]:
            expression_states[4].goto_dict[first] = [[args_states[0], expression_states[6]], [], ["#set_return_line #assert_args_count #call_func"],False]
        for follow in cs.Follow["args"]:
            expression_states[4].goto_dict[follow] = [[expression_states[6]], [], ["#set_return_line #assert_args_count #call_func"],True]

        for first in cs.First["term"]:
            expression_states[5].goto_dict[first] = [[term_states[0], expression_states[10]], [], ["#assert_type_check #mult"],False]

        expression_states[6].goto_dict[")"] = [[expression_states[9]], [], [],False]

        expression_states[7].goto_dict[")"] = [[expression_states[9]], [], [],False]

        for first in cs.First["expression"]:
            expression_states[8].goto_dict[first] = [[expression_states[0], expression_states[13]], [], ["#assert_type_check #assign_and_keep"],False]

        for first in cs.First["term-extension"]:
            expression_states[9].goto_dict[first] = [[term_extension_states[0], expression_states[10]], [], [],False]
        for follow in cs.Follow["term-extension"]:
            expression_states[9].goto_dict[follow] = [[expression_states[10]], [], [],True]

        for first in cs.First["additive-expression-extension"]:
            expression_states[10].goto_dict[first] = [[additive_expression_extension_states[0], expression_states[11]], [], [],False]
        for follow in cs.Follow["additive-expression-extension"]:
            expression_states[10].goto_dict[follow] = [[expression_states[11]], [], [],True]

        for first in cs.First["relop"]:
            expression_states[11].goto_dict[first] = [[relop_states[0], expression_states[12]], [], [],False]
        for follow in cs.Follow["expression"]:
            expression_states[11].goto_dict[follow] = [[expression_states[13]], [], [], True]

        for first in cs.First["additive-expression"]:
            expression_states[12].goto_dict[first] = [[additive_expression_states[0], expression_states[13]], [], ["#assert_operation_type #operate"],False]

        expression_states[13].is_final = True


        #------- expression stmt


        for first in cs.First["expression"]:
            expression_stmt_states[0].goto_dict[first] = [[expression_states[0], expression_stmt_states[1]], [], ["#pop"], False]
        expression_stmt_states[0].goto_dict["continue"] = [[expression_stmt_states[1]], [], ["#assert_in_while #jp_continue_address"], False]
        expression_stmt_states[0].goto_dict["break"] = [[expression_stmt_states[1]], [], ["#assert_in_while #jp_to_break"], False]
        expression_stmt_states[0].goto_dict[";"] = [[expression_stmt_states[2]], [], [], False]
        expression_stmt_states[1].goto_dict[";"] = [[expression_stmt_states[2]], [], [], False]
        expression_stmt_states[2].is_final = True


        # ------- statement

        for first in cs.First["expression-stmt"]:
            statement_state[0].goto_dict[first] = [[expression_stmt_states[0], statement_state[1]], [], [],False]

        for first in cs.First["coumpound-stmt"]:
            statement_state[0].goto_dict[first] = [[compound_stmt_states[0], statement_state[1]], [], [],False]

        for first in cs.First["selection-stmt"]:
            statement_state[0].goto_dict[first] = [[selection_stmt_states[0], statement_state[1]], [], [],False]

        for first in cs.First["iteration-stmt"]:
            statement_state[0].goto_dict[first] = [[iteration_stmt_states[0], statement_state[1]], [], [],False]

        for first in cs.First["return-stmt"]:
            statement_state[0].goto_dict[first] = [[return_stmt_states[0], statement_state[1]], [], [],False]

        for first in cs.First["switch-stmt"]:
            statement_state[0].goto_dict[first] = [[switch_stmt_states[0], statement_state[1]], [], [],False]

        statement_state[1].is_final = True

        # ------- selection stmt

        selection_stmt_states[0].goto_dict["if"] = [[selection_stmt_states[1]], [], [], False]
        selection_stmt_states[1].goto_dict["("] = [[selection_stmt_states[2]], [], [], False]
        for first in cs.First["expression"]:
            selection_stmt_states[2].goto_dict[first] = [[expression_states[0], selection_stmt_states[3]], [], [], False]
        selection_stmt_states[3].goto_dict[")"] = [[selection_stmt_states[4]], [], ["#save_line"], False]
        for first in cs.First["statement"]:
            selection_stmt_states[4].goto_dict[first] = [[statement_state[0], selection_stmt_states[5]],[],["#save_line"],False]
        selection_stmt_states[5].goto_dict["else"] = [[selection_stmt_states[6]], [], ["#write_jpf"], False]
        for first in cs.First["statement"]:
            selection_stmt_states[6].goto_dict[first] = [[statement_state[0], selection_stmt_states[7]], [], ["#write_jp"], False]
        selection_stmt_states[7].is_final = True


        # ----- iteration stmt


        iteration_stmt_states[0].goto_dict["while"] = [[iteration_stmt_states[1]], [], ["#push_break_stack #push_continue_stack "], False]
        iteration_stmt_states[1].goto_dict["("] = [[iteration_stmt_states[2]], [], [], False]
        for first in cs.First["expression"]:
            iteration_stmt_states[2].goto_dict[first] = [[expression_states[0], iteration_stmt_states[3]], [], ["#jpf_to_break"], False]
        iteration_stmt_states[3].goto_dict[")"] = [[iteration_stmt_states[4]], [], [], False]
        for first in cs.First["statement"]:
            iteration_stmt_states[4].goto_dict[first] = [[statement_state[0], iteration_stmt_states[5]], [], ["#jp_continue_address #set_top_break_value #pop_break_top #pop_continue"], False]
        iteration_stmt_states[5].is_final = True


        # ------ return stmt

        return_stmt_states[0].goto_dict["return"] = [[return_stmt_states[1]], [], [], False]
        return_stmt_states[1].goto_dict[";"] = [[return_stmt_states[3]], [], ["#assert_func_void #jp_to_caller"], False]
        for first in cs.First["expression"]:
            return_stmt_states[1].goto_dict[first] = [[expression_states[0], return_stmt_states[2]], [], ["#assert_func_int #set_return_value #jp_to_caller"], False]
        return_stmt_states[2].goto_dict[";"] = [[return_stmt_states[3]], [], [], False]
        return_stmt_states[3].is_final = True

        # ------- case stmt

        case_stmt_states[0].goto_dict["case"] = [[case_stmt_states[1]], [], [],False]
        case_stmt_states[1].goto_dict["NUM"] = [[case_stmt_states[2]], [], ["#push_constant #compare_save_for_jpf"],False]
        case_stmt_states[2].goto_dict[":"] = [[case_stmt_states[3]], [], [],False]
        for first in cs.First["statement"]:
            case_stmt_states[3].goto_dict[first] = [[statement_state[0], case_stmt_states[3]], [], [],False]
        for follow in cs.Follow["case-stmt"]:
            case_stmt_states[3].goto_dict[follow] = [[case_stmt_states[4]], [], ["#jp_to_break #jpf_set_for_case"], True]
        case_stmt_states[4].is_final = True

        # ------ switch stmt


        switch_stmt_states[0].goto_dict["switch"] = [[switch_stmt_states[1]], [], ["#push_break_stack "], False]
        switch_stmt_states[1].goto_dict["("] = [[switch_stmt_states[2]], [], [], False]
        for first in cs.First["expression"]:
            switch_stmt_states[2].goto_dict[first] = [[expression_states[0], switch_stmt_states[3]], [], [], False]
        switch_stmt_states[3].goto_dict[")"] = [[switch_stmt_states[4]], [], [], False]
        switch_stmt_states[4].goto_dict["{"] = [[switch_stmt_states[5]], [], [], False]
        for first in cs.First["case-stmts"]:
            switch_stmt_states[5].goto_dict[first] = [[case_stmt_states[0], switch_stmt_states[5]], [], [], False]
        for first in cs.First["default-stmt"]:
            switch_stmt_states[5].goto_dict[first] = [[default_stmt_states[0], switch_stmt_states[6]], [], ["#set_top_break_value #pop_break_top"], False]
        for follow in cs.Follow["default-stmt"]:
            switch_stmt_states[5].goto_dict[follow] = [[switch_stmt_states[6]], [], ["#set_top_break_value #pop_break_top"], True]
        switch_stmt_states[6].goto_dict["}"] = [[switch_stmt_states[7]], [], ["#pop"], False]

        switch_stmt_states[7].is_final = True

        # ------ default stmt

        default_stmt_states[0].goto_dict["default"] = [[default_stmt_states[1]], [], [], False]
        default_stmt_states[1].goto_dict[":"] = [[default_stmt_states[2]], [], [], False]
        for first in cs.First["statement"]:
            default_stmt_states[2].goto_dict[first] = [[statement_state[0], default_stmt_states[2]], [], [], False]
        for follow in cs.Follow["default-stmt"]:
            default_stmt_states[2].goto_dict[follow] = [[default_stmt_states[3]], [], [], True]
        default_stmt_states[3].is_final = True

        # ------ param

        param_state[0].goto_dict["int"] = [[param_state[1]], [], ["#p_type"],False]
        param_state[0].goto_dict["void"] = [[param_state[1]], [], ["#p_type"],False]
        param_state[1].goto_dict["ID"] = [[param_state[2]], [], ["#p_id"],False]
        for first in cs.First["param-extension"]:
            param_state[2].goto_dict[first] = [[param_extension_state[0], param_state[3]], [], [],False]
        for follow in cs.Follow["param-extension"]:
            param_state[2].goto_dict[follow] = [[param_state[3]], [], ["#declare_param_int"], True]
        param_state[3].is_final = True

        # ------ param-extension

        param_extension_state[0].goto_dict["["] = [[param_extension_state[1]], [], [],False]
        param_extension_state[1].goto_dict["]"] = [[param_extension_state[2]], [], ["#declare_param_arr"],False]
        for follow in cs.Follow["param-extension"]:
            param_extension_state[0].goto_dict[follow] = [[param_extension_state[2]], [], ["#declare_param_int"], True]
        param_extension_state[2].is_final = True

        # ------ param list

        for first in cs.First["param"]:
            param_list_state[0].goto_dict[first] = [[param_state[0], param_list_state[1]], [], ["#push_param_in_func"],False]
        for follow in cs.Follow["param-list"]:
            param_list_state[1].goto_dict[follow] = [[param_list_state[3]], [], [], True]
        param_list_state[1].goto_dict[","] = [[param_list_state[2]], [], [], False]
        for first in cs.First["param-list"]:
            param_list_state[2].goto_dict[first] = [[param_list_state[0], param_list_state[3]], [], [],False]
        param_list_state[3].is_final = True

        # ------ params

        params_state[0].goto_dict["int"] = [[params_state[2]], [], ["#p_type"],False]
        params_state[0].goto_dict["void"] = [[params_state[1]], [], [],False]
        params_state[1].goto_dict["ID"] = [[params_state[3]], ["#p_type"], ["#p_id"],False]
        for follow in cs.Follow["params"]:
            params_state[1].goto_dict[follow] = [[params_state[6]], ["#declare_zero_params_func"], [], True]
        params_state[2].goto_dict["ID"] =[[params_state[3]], [], ["#p_id"],False]
        for first in cs.First["param-extension"]:
            params_state[3].goto_dict[first] = [[param_extension_state[0], params_state[4]], [], ["#push_param_in_func"],False]
        for follow in cs.Follow["param-extension"]:
            params_state[3].goto_dict[follow] = [[params_state[4]], [], ["#declare_param_int #push_param_in_func"], True]
        for follow in cs.Follow["params"]:
            params_state[3].goto_dict[follow] = [[params_state[6]], [], ["#declare_param_int #push_param_in_func"], True]
        params_state[4].goto_dict[","] = [[params_state[5]], [], [],False]
        for follow in cs.Follow["params"]:
            params_state[4].goto_dict[follow] = [[params_state[6]], [], [], True]
        for first in cs.First["param-list"]:
            params_state[5].goto_dict[first] = [[param_list_state[0], params_state[6]], [], [],False]

        params_state[6].is_final = True







