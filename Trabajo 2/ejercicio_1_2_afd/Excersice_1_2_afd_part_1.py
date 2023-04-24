# (aa/b)*
from Constant import *
from String import *

class Excersice_1_2_afd_part_1:
    def __init__(self):
        self.__is_part_2 = False

    def take_print(self, value):
        print(value)

    def add_aa_b_in_string(self):
        letter_input = str(input(INPUT_AA_B))
        return letter_input

    def verificate_if_aa_b(self, letter_input_value, string):
        if letter_input_value == "aa" or letter_input_value == "b":
            string.set_string(string.get_string() + letter_input_value)
        elif letter_input_value == "$":
            self.__is_part_2 = True
        else:
            self.take_print(ERROR_NO_AA_B)

    def start(self, string):
        self.take_print("ESTADO A")
        while not self.__is_part_2:
            self.verificate_if_aa_b(self.add_aa_b_in_string(), string)