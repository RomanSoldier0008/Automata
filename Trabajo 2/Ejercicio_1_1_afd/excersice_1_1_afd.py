from constant import *
from sys import exit

class Excersice_1_1_afd:
    def __init__(self):
        self.__input_letter = ""
        self.__string = ""
        self.__status = "A"

    def print(self, value):
        print(value)

    def start_status(self):
        self.print("Estado A")
        while self.__input_letter != "a" and self.__input_letter != "b":
            self.__input_letter = str(input(INPUT))
            if self.__input_letter == "a" or self.__input_letter == "b":
                self.__string += self.__input_letter
        self.verificate_input_letter()

    def verificate_input_letter(self):
        if self.__input_letter == "$":
            self.print(exit(EXIT_FAREWELL.format(self.__string)))

        if self.__input_letter == "a":
            self.print("Estado B")
            self.start_status_b()

        elif self.__input_letter == "b":
            self.print("Estado C")
            self.start_status_c()

        else:
            self.reset_input_letter()
            self.print(ERROR)
            self.start_status()

    def start_status_b(self):
        while self.__input_letter == "a":
            self.__input_letter = str(input(INPUT))
            self.__string += self.__input_letter
        self.verificate_input_letter()

    def start_status_c(self):
        while self.__input_letter == "b":
            self.__input_letter = str(input(INPUT))
            self.__string += self.__input_letter
        self.verificate_input_letter()

    def reset_input_letter(self):
        self.__input_letter = ""

excersice = Excersice_1_1_afd()
excersice.start_status()