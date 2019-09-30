
class Stack:
    def __init__(self):
        self.list = []
        self.top_index = 0

    def pop(self,n = 1):
        if len(self.list) == 0:
            print("Error: parse stack is empty")
            return
        else:
            top = self.list[self.top_index-1]
            self.list = self.list[:-n]
            self.top_index -= n
            return top

    def top(self):
        return self.list[self.top_index-1]

    def push(self, element):
        self.top_index += 1
        self.list.append(element)

    def prin(self):
        print([info.token for info in self.list])