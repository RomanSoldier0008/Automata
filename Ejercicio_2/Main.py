from Sub_menu import *


class Main:
    def __init__(self):
        self.__option = 0

    def print(self, print_value):
        print(print_value)

    def choose_menu(self, id_value):
        if id_value == GO_TO_MAIN:
            self.print(PRINT_MENU_MAIN)

    def input_option(self):
        try:
            self.__option = int(input(ENTER_OPTION))
        except ValueError:
            self.print(VALUE_ERROR)

    def create_sub_menu(self):
        sub_menu = Sub_menu()
        return sub_menu

    def start(self):
        while self.__option != BUTTOM_EXIT_MAIN:
            self.choose_menu(GO_TO_MAIN)
            self.input_option()
            if self.__option == GO_TO_SUB_MENU:
                self.create_sub_menu().start()

menu = Main()
menu.start()