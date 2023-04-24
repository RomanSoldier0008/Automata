from Constant import *
from Excersice_1_2_afd_part_1 import Excersice_1_2_afd_part_1
from Excersice_1_2_afd_part_2 import Excersice_1_2_afd_part_2
from String import *

class Main:
    def __init__(self):
        self.__option_menu = 0

    def take_print(self, value):
        print(value)

    def start(self):
        while True:
            try:
                self.__option_menu = int(input(OPTION_MENU_INPUT))
            except ValueError:
                self.take_print(VALUE_ERROR)

            if self.__option_menu == 1:
                string = String()
                excersice_part_1 = Excersice_1_2_afd_part_1()
                excersice_part_2 = Excersice_1_2_afd_part_2()
                excersice_part_1.start(string)
                excersice_part_2.start(string)

            elif self.__option_menu == 2:
                break

menu = Main()
menu.start()