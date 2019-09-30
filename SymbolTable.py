from Stack import Stack
import constants as cs

class IdInfo:
    def __init__(self, token, size = None, type = None, addressing_mode = None):
        self.token = token
        self.address = None
        self.type = type
        self.size = size
        self.is_array = None
        self.array_size = None
        self.addressing_mode = addressing_mode
        self.is_function = False
        self.starting_line = None
        self.params_count = None
        self.params_type = []
        self.current_param = None
        self.line = None

    def address_in_program(self):
        if self.addressing_mode == cs.DIRECT:
            return str(self.address)
        elif self.addressing_mode == cs.INDIRECT:
            return "@"+str(self.address)
        elif self.addressing_mode == cs.IMMEDIATE:
            return "#"+self.token
        else:
            return "#"+self.token

    def address_for_func(self):
        if self.addressing_mode == cs.IMMEDIATE:
            return "#"+str(self.token)
        elif not self.is_array:
            return str(self.address)
        elif self.is_array:
            return "#" + str(self.address)


class SymbolTable:
    def __init__(self):
        self.scope_stack = Stack()
        self.declaration_usage_not = False

    def find(self, id_token):
        if self.declaration_usage_not:
            top_scope = self.scope_stack.top()
            for id_info in top_scope:
                if id_info.token == id_token:
                    return id_info
        else:
            for scope in reversed(self.scope_stack.list):
                for id_info in scope:
                    if id_info.token == id_token:
                        return id_info
        new_id = IdInfo(id_token)
        self.scope_stack.top().append(new_id)
        return new_id

    def new_scope(self):
        self.scope_stack.push([])

    def delete_scope(self):
        self.scope_stack.pop(1)