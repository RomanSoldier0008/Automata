from Constant import *

class Excersice_1_2_afd_part_2:
    def __init__(self):
        self.__is_finish = False

    def take_print(self, value):
        print(value)

    def add_a_bb_in_string(self):
        letter_input = str(input(INPUT_A_BB))
        return letter_input

    def verificate_if_aa_b(self, letter_input_value, string):
        if letter_input_value == "a" or letter_input_value == "bb":
            string.set_string(string.get_string() + letter_input_value)
        elif letter_input_value == "$":
            self.__is_finish = True
        else:
            self.take_print(ERROR_NO_A_BB)

    def start(self, string):
        self.take_print("ESTADO B")
        while not self.__is_finish:
            self.verificate_if_aa_b(self.add_a_bb_in_string(), string)
        self.take_print(string.get_string())