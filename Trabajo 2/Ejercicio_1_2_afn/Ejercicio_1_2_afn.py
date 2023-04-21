# (aa|b)* (a|bb)*
from Constant import *

class Ejercicio_1_2_afn:
    def __init__(self):
        self.__list_1 = []
        self.__string_1 = ""
        self.__list_2 = []
        self.__string_2 = ""
        self.__result_string = ""
        self.__status = 0

    def print(self, value):
        print(value)

    def add_string_1(self):
        while self.__status == 0:
            self.accept_string_1(str(input(ADD_STRING_INPUT)))

    def add_string_2(self):
        while self.__status == 1:
            self.accept_string_2(str(input(ADD_STRING_INPUT_PART_2)))

    def accept_string_1(self, value_string):
        self.__list_1.append(value_string)
        for character in self.__list_1:
            if character == "aa" or character == "b":
                self.__status = 1
            elif character == "":
                continue

    def accept_string_2(self, value_string):
        self.__list_2.append(value_string)
        for character in self.__list_2:
            if character == "a" or character == "bb":
                self.__status = 2
            elif character == "":
                continue

    def delete_invalid_characters_in_string_1(self):
        for i in range(len(self.__list_1)):
            if self.__list_1[i] == 'aa' or self.__list_1[i] == 'b':
                self.__string_1 += self.__list_1[i]

    def delete_invalid_characters_in_string_2(self):
        for i in range(len(self.__list_2)):
            if self.__list_2[i] == 'a' or self.__list_2[i] == 'bb':
                self.__string_2 += self.__list_2[i]
                self.__result_string = self.__string_1 + self.__string_2

    def start(self):
        self.print(STATUS.format(self.__status))
        self.add_string_1()
        self.delete_invalid_characters_in_string_1()
        self.print(STATUS.format(self.__status))
        self.add_string_2()
        self.delete_invalid_characters_in_string_2()
        self.print(self.__result_string)
        self.print(STATUS.format(self.__status))

exercise = Ejercicio_1_2_afn()
exercise.start()