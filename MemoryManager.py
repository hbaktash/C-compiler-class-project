from SymbolTable import IdInfo

Default_Type = 4

class MemoryManager:
    def __init__(self, start_index):  # infinite memory
        self.memory = []
        self.current_index = start_index

    def get_temp(self, id_info : IdInfo):
        id_address = self.current_index
        self.current_index += id_info.size
        return id_address
