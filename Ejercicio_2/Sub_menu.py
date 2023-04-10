from String_calculator import *
from Constant import *

class Sub_menu:
    def __init__(self):
        self.__option = 0
        self.__object_string = None

    def set_object_string(self, object_value):
        self.__object_string = object_value

    def get_object_string(self):
        return self.__object_string

    def print(self, print_value):
        print(print_value)

    def go_to_menu(self, id_value):
        if id_value == GO_TO_SUB_MENU:
            self.print(PRINT_SUB_MENU)

    def input_option(self):
        try:
            self.__option = int(input(ENTER_OPTION))
        except ValueError:
            self.print(VALUE_ERROR)

    def if_buttom_solve(self, string):
        if self.__option == BUTTOM_RUN:
            string.solve()
            string.print()

    def start(self):
        if self.__option == BUTTOM_EXIT_SUB_MENU:
            self.__object_string = None
            return
        self.create_string_calculator_object()
        self.go_to_menu(GO_TO_SUB_MENU)
        self.input_option()
        self.if_buttom_solve(self.__object_string)

    def create_string_calculator_object(self):
        if self.__object_string is None:
            string = String_calculator()
            string.set_string(str(input(ENTER_STRING)))
            self.__object_string = string
            self.delete_character_if_not_is_a_digit()

    def delete_character_if_not_is_a_digit(self):
        string = ""
        for character in self.__object_string.get_string():
            if character == "+" or character == "*" or character.isdigit():
                string += character
            else:
                string = string.replace(character, "")
        self.__object_string.set_string(string)