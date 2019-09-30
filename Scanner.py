from SymbolTable import IdInfo, SymbolTable
import constants as cs
OTHER = cs.OTHER
ID = cs.ID
NUM = cs.NUM

import ErrorHandler


class Scanner(object):
    def __init__(self, input_code, symbol_table: SymbolTable):
        self.symbol_table = symbol_table
        self.current_location = 0
        self.token_beginning = 0
        # self.error_handler = ErrorHandler(self)
        self.input_code = input_code
        self.prev_token = None

    def get_char(self):
        if self.current_location >= len(self.input_code):
            return -1
        char = self.input_code[self.current_location]
        self.current_location += 1
        return char

    def get_back(self):  #works as a temp parameter
        self.current_location -= 1

    def look_ahead(self):
        if self.prev_token == "EOF":
            self.prev_token = "$"
            return "$", "$"

        if self.prev_token == "$":
            print("Scanner: Reached end of file", self.current_location)
            return


        self.token_beginning = self.current_location
        char = self.get_char()

        # ------    handle equal == or =   -----
        if char == "=":
            next_char = self.get_char()
            if (next_char == -1):
                print("error in input")
            if (next_char == "="):
                token = "=="
                self.prev_token = token
                return IdInfo(token,type="op"), token
            else:
                token = "="
                self.get_back()
                self.prev_token = token
                return token, token

        # ------    handle + -   -----
        if char == "+" or char == "-":
            if self.prev_token in cs.operators or self.prev_token in cs.opening_tokens or self.prev_token in cs.separator_tokens:
                number = char
                last_char = char
                while last_char.isdigit() or last_char == "+" or last_char == "-":
                    next_char = self.get_char()
                    if (next_char == -1):
                        self.prev_token = int(number)
                        return IdInfo(str(int(number)),type=cs.INT, addressing_mode=cs.IMMEDIATE), NUM
                    if (next_char.isdigit()):
                        number += next_char
                    elif next_char in cs.Terminals or next_char in cs.whitespace:
                        self.get_back()
                        self.prev_token = int(number)
                        return IdInfo(str(int(number)),type=cs.INT, addressing_mode=cs.IMMEDIATE), NUM
                    else:
                        print("Scanner Error: Invalid character in number")
                        print("Panic Mode: Ignore character in Number ", next_char)
                        return self.look_ahead()
            else:
                self.prev_token = char
                return IdInfo(char, type=cs.OPERATION), char

        # ------    handle numbers   ------
        elif char.isdigit():
            number = char
            last_char = char
            while last_char.isdigit() or last_char == "+" or last_char == "-":
                next_char = self.get_char()
                last_char = next_char
                if (next_char == -1):
                    self.prev_token = int(number)
                    return IdInfo(str(int(number)),type=cs.INT, addressing_mode=cs.IMMEDIATE), NUM
                if (next_char.isdigit()):
                    number += next_char
                elif next_char in cs.Terminals or next_char in cs.whitespace:
                    self.get_back()
                    self.prev_token = int(number)
                    return IdInfo(str(int(number)),type=cs.INT, addressing_mode=cs.IMMEDIATE), NUM
                else:
                    print("Scanner Error: Invalid character in number")
                    print("Panic Mode: Ignore character in Number ", next_char)
                    return self.look_ahead()

        # -----     handle one char cs.Terminals  -----
        elif char in cs.Terminals:
            self.prev_token = char
            if char in cs.operators:
                return IdInfo(char,type=cs.OPERATION), char
            return char, char


        # ----- handle ID or keywords ------
        elif char.isalpha():
            current_ID = char
            last_char = char
            while last_char.isdigit() or last_char.isalpha():
                next_char = self.get_char()
                last_char = next_char
                if next_char == -1:
                    self.prev_token = current_ID
                    if (current_ID in cs.key_words):
                        return IdInfo(current_ID,type=current_ID), current_ID
                    else:
                        return self.symbol_table.find(current_ID), ID  # returns an IdInfo object
                    # return current_ID, ID
                if next_char.isdigit() or next_char.isalpha():
                    current_ID += next_char
                elif next_char in cs.Terminals or next_char in cs.whitespace:
                    self.get_back()
                    self.prev_token = current_ID
                    if (current_ID in cs.key_words):
                        return IdInfo(current_ID,type=current_ID), current_ID
                    else:
                        return self.symbol_table.find(current_ID), ID  # returns an IdInfo object
                else:
                    print("Scanner Error: Invalid character in identifier")
                    print("Panic Mode: Ignore character in ID ", next_char)
                    return self.look_ahead()

        # ----- handle comments ----
        elif char == "/":
            next_char = self.get_char()
            if next_char != "*":
                print("Scanner Error: Invalid character")
                print("Panic Mode: Ignore character / ")
                return self.look_ahead()

            next_char = self.get_char()
            while next_char != "*" and next_char != -1:
                next_char = self.get_char()
            if next_char == -1:
                print("Scanner Error: Unexpected end of file")
                return
                # print("Panic Mode: Ignore character in Number ", next_char)
                # return self.look_ahead()

            elif next_char == "*":
                next_char = self.get_char()
                if next_char == "/":
                    return self.look_ahead()
                elif next_char == -1:
                    print("Scanner Error: Unexpected end of file", self.current_location - 1)
                    return
                else:
                    print("Scanner Error: Invalid character")
                    print("Panic Mode: Ignore character in * ", next_char)
                    return self.look_ahead()


        # ------- handle cs.whitespace -------
        elif char in cs.whitespace:
            return self.look_ahead()

        else:
            print("Scanner Error: Invalid character", self.current_location)
            print("Panic Mode: Ignore character ", char)
            return self.look_ahead()

# symbol_t = SymbolTable()
# symbol_t.new_scope()
# scanner = Scanner("if(1)"
#                   ";"
#                   "else b= 1;", symbol_table=symbol_t)
# print(scanner.look_ahead())
# print(scanner.look_ahead())
# print(scanner.look_ahead())
# print(scanner.look_ahead())
# print(scanner.look_ahead())
# print(scanner.look_ahead())
# print(scanner.look_ahead())



