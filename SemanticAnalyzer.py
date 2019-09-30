from TransitionDiagram import Routine


class SemanticAnalyzer:
    def __init__(self, symbol_table, semantic_stack, memory_manager):
        self.symbol_table = symbol_table
        self.ss = semantic_stack
        self.memory_manager = memory_manager

    def run_routine(self, routine : Routine):
        pass
