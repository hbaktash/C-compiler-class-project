IMMEDIATE = "immediate"
INDIRECT = "indirect"
DIRECT = "direct"

OPERATION = "op"
INT = "int"
OTHER = "other_token"
ID = "ID"
NUM = "NUM"
VOID = "void"
TYPE = "type"
operators = ["+", "-", "=", "*", "<", "=="]

Terminals = ['(', ')', '*', '+', '"', '"', '-', ';', '<', '=', '[', ']', 'ID', 'EOF', 'if', 'int', 'NUM', '==',
             'return', 'else', 'void', 'while', '{', '}', '$', ',', 'output', ':']
key_words = ["EOF", "ID", "NUM", "void", "continue", "break", "if", "while", "return", "switch", "case", "default", "else", "int"]
operators = ["+", "-", "=", "*", "<", "=="]
opening_tokens = ["[", "(", "{"]
separator_tokens = [",", ";"]
whitespace = ["\n", " ", "\t", "\r"]

First = {
    "program": ["EOF", "int", "void"],
    "declaration-list": ["Eps", "int", "void"],
    "declaration": ["int", "void"],
    "var-declaration-extension": [";", "["],
    "var-delaration": ["int", "void"],
    "type-specifier": ["int", "void"],
    "fun-declaration": ["int", "void"],
    "params": ["int", "void"],
    "param-list": ["int", "void"],
    "param-list-extension": [",", "Eps"],
    "param-extension": ["[", "Eps"],
    "param": ["int", "void"],
    "coumpound-stmt": ["{"],
    "statement-list": ["Eps", "{", "continue", "break", ";", "if", "while", "return", "switch", "ID", "(", "NUM"],
    "statement": ["{", "continue", "break", ";", "if", "while", "return", "switch", "ID", "(", "NUM"],
    "expression-stmt": ["continue", "break", ";", "ID", "(", "NUM"],
    "selection-stmt": ["if"],
    "iteration-stmt": ["while"],
    "return-stmt": ["return"],
    "switch-stmt": ["switch"],
    "case-stmts": ["case", "Eps"],
    "case-stmt": ["case"],
    "default-stmt": ["default", "Eps"],
    "expression": ["ID", "NUM", "("],
    "var": ["ID"],
    "var-extension": ["[", "Eps"],
    "simple-expression-extension": ["<", "==", "Eps"],
    "simple-expression": ["(", "ID", "NUM"],
    "relop": ["<", "=="],
    "additive-expression": ["ID", "NUM", "("],
    "additive-expression-extension": ["+","-","Eps"],
    "addop": ["+", "-"],
    "term-extension": ["*", "Eps"],
    "term": ["(", "ID", "NUM"],
    "factor": ["(", "ID", "NUM"],
    "call": ["ID"],
    "args": ["Eps", "ID", "(", "NUM"],
    "arg-list-extension": [",", "Eps"],
    "arg-list": ["ID", "(", "NUM"]
}
Follow = {
    "program": ["$"],
    "declaration-list": ["EOF", "{", "continue", "break", ";", "if", "while", "return", "switch", "ID", "("
        , "NUM", "}"],
    "declaration": ["int", "void", "EOF", "{", "continue", "break", ";", "if", "while", "return", "switch", "ID", "("
        , "NUM", "}"],
    "var-declaration-extension": ["int", "void", "EOF", "{", "continue", "break", ";", "if", "while", "return", "switch", "ID", "("
        , "NUM", "}"],
    "var-delaration": ["int", "void", "EOF", "{", "continue", "break", ";", "if", "while", "return", "switch", "ID", "("
        , "NUM", "}"],
    "type-specifier": ["ID"],
    "fun-declaration": ["int", "void", "EOF", "{", "continue", "break", ";", "if", "while", "return", "switch", "ID", "("
        , "NUM", "}"],
    "params": [")"],
    "param-list": [")"],
    "param-list-extension": [")"],
    "param-extension": [",", ")"],
    "param": [",", ")"],
    "coumpound-stmt": ["int", "void", "EOF", "{", "continue", "break", ";", "if", "while", "return",
                       "switch", "ID", "(", "NUM","}", "else", "case", "default"],
    "statement-list": ["}", "case", "default"],
    "statement": ["{", "continue", "break", ";", "if", "while", "return", "switch", "ID", "(", "NUM", "}",
                  "else", "case", "default"],
    "expression-stmt": ["{", "continue", "break", ";", "if", "while", "return", "switch", "ID", "(", "NUM", "}",
                  "else", "case", "default"],
    "selection-stmt": ["{", "continue", "break", ";", "if", "while", "return", "switch", "ID", "(", "NUM", "}",
                  "else", "case", "default"],
    "iteration-stmt": ["{", "continue", "break", ";", "if", "while", "return", "switch", "ID", "(", "NUM", "}",
                  "else", "case", "default"],
    "return-stmt": ["{", "continue", "break", ";", "if", "while", "return", "switch", "ID", "(", "NUM", "}",
                  "else", "case", "default"],
    "switch-stmt": ["{", "continue", "break", ";", "if", "while", "return", "switch", "ID", "(", "NUM", "}",
                  "else", "case", "default"],
    "case-stmts": ["default", "}"],
    "case-stmt": ["case", "default", "}"],
    "default-stmt": ["}"],
    "expression": [";", ")", "]", ","],
    "var": ["=", "*", "+", "-", "<","==",";",")","]",","],
    "var-extension": ["=", "*", "+", "-", "<","==",";",")","]",","],
    "simple-expression-extension": [";", ")", "]", ","],
    "simple-expression": [";", ")", "]", ","],
    "relop": ["(", "ID", "NUM"],
    "additive-expression": ["<", "==", ";", ")", "]", ","],
    "additive-expression-extension": ["<", "==", ";", ")", "]", ","],
    "addop": ["(", "ID", "NUM"],
    "term-extension": ["+", "-", "<", "==", ";",")","]",","],
    "term": ["+", "-", "<", "==", ";",")","]",","],
    "factor": ["+", "-", "<", "==", ";",")","]",",","*"],
    "call": ["+", "-", "<", "==", ";",")","]",",","*"],
    "args": [")"],
    "arg-list-extension": [")"],
    "arg-list": [")"],
}

Grammer = [
    "program #output_func_declare #new_scope declaration-list EOF #main_check #delete_scope",  ###TODO maincheck declare and keep
    "declaration-list decleration declaration-list | Eps",  ###
    "declaration var-declaration | fun-declaration",  ###
    "var-declaration  #start_declaration type-specifier ID #p_id var-declaration-extension #end_declaration",  ###
    "var-declaration-extension #declare_int ; | [ Num #push_constant ] #declare_arr ;", ###
    "type-specifier int #p_type | void #p_type",  ###

    "fun-declaration type-specifier ID #push_function_id #new_scope ( #save_fun_line_address_and_save_line params ) compound-stmt #jp_to_caller_final #delete_scope",  ###
    "params param-list | void #declare_zero_params_func",  ###
    "param-list param #push_param_in_func param-list-extension",  ###
    "param-list-extension Eps | , param-list",  ###
    "param type-specifier ID #p_id param-extension",  ###
    "param-extension Eps #declare_param_int | [] #declare_param_arr",  ###

    "compound-stmt { #new_scope declaration-list statement-list #delete_scope }",  ###
    "statement-list statement statement-list | Eps", ###
    "statement expression-stmt | compound-stmt | selection-stmt | iteration-stmt | return-stmt | switch-stmt",  ###

    "expression-stmt expression ; #pop | continue ; #assert_in_while #jp_to_save_for_continue | break ; #assert_in_while #jp_to_save_for_break | ;",  ###

    "selection-stmt if ( expression ) #save_line statement #save_line else #write_jpf statement #write_jp",  ###

    "iteration-stmt while #push_while_identifier #push_for_break #save_line ( expression #jpf_while_break ) statement #jp_to_top_while #set_break_address #pop_while_identifier",  ###
    
    "XXX iteration-stmt while #push_break_stack #push_continue_stack ( expression #jpf_to_break ) statement #jp_continue_address #set_top_break_value #pop_break_top #pop_continue",  ### $$$
    
    "XXX expression-stmt expression ; #pop | continue ; #assert_in_while #jp_to_continue | break ; #assert_in_while #jp_to_break | ;",  ### $$$

    "return-stmt return return-stmt-extension #jp_to_caller; ",  ###
    "return-stmt-extension Eps #assert_func_void | expression #assert_func_int #set_return_value",  ###


    "switch-stmt switch #push_break_stack ( expression ) { case-stmts default-stmt #set_top_break_value #pop_break_top} #pop ",    ###  $$$

    "case-stmts case-stmt case-stmts | Eps",  ###

    "case-stmt case NUM #push_constant #compare_save_for_jpf : statement-list #jp_to_save_for_break #jpf_set_for_case",  ###

    "default-stmt default : statement-list | Eps",  ###


    "expression var = expression #assert_type_check #assign_and_keep | simple-expression",  ###
    "var ID #p_id var-extension",  ###
    "var_extension Eps #assert_type_int | #assert_arr [ expression #assert_index ] #p_arr_value",  ###
    "simple-expression additive-expression simple-expression-extension",  ###
    "simple-expression-extension relop additive-expression #assert_operation_type #operate | Eps"  ###
    "relop < #p_operation | == #p_operation",  ###
    "additive-expression term additive-expression-extension ",  ###
    "additive-expression-extension addop additive-expression #assert_operation_type #operate | Eps",  ###
    "addop + #p_operation | - #p_operation",  ###
    "term factor term-extension "  ###
    "term-extension * term #assert_type_check #mult| Eps",  ###
    "factor ( expression ) | var | call | NUM #push_constant",  ###

    "call ID #p_func_id ( args ) #set_return_line #assert_args_count #call_func ",  ###
    "args arg-list | Eps",  ###
    "arg-list expression #assert_arg_type #put_arg arg-list-extension",  ###
    "arg-list-extension  , arg-list | Eps"  ###
]
