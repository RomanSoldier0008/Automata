from Constant import *

class Ejercicio_1_1_afn:
    def __init__(self):
        self.__string = ""
        self.__ejecuted = True
        self.__status = ""

    def add_string(self):
        self.__string = str(input(ADD_STRING_INPUT))

    def add_string_to_string(self):
        self.__string += str(input(ADD_STRING_INPUT))

    def delete_character_finished(self):
        new_string = self.__string
        count_list = len(self.__string) - 1
        for i in range(0, len(self.__string)):
            if self.__string[i] == "$" and i < count_list:
                if self.__string[count_list] == "$":
                    new_string = new_string.replace("$", "")
                    new_string += "$"
                else:
                    new_string = new_string.replace("$", "")
        self.__string = new_string

    def verificate_string(self):
        for character in self.__string:
            if character == "a" or character == "b" or character == "" or character == "$":
                continue
            else:
                return False
        return True

    def finish_the_program(self):
        for i in range(0, len(self.__string)):
            continue
        if "a" in self.__string or "b" in self.__string:
            if self.__string[i] == "$":
                self.__ejecuted = False
                return True
        return False

    def print(self, print_value):
        print(print_value)

    def program_ejecuting(self):
        self.print(self.go_to_status_0())
        self.add_string()
        while self.__ejecuted:
            self.delete_character_finished()
            if self.verificate_string():
                self.print(self.go_to_status_1())
                if self.finish_the_program():
                    self.print(self.go_to_status_2())
                    self.print(self.__string)
                else:
                    self.print(self.go_to_status_0())
                    self.add_string_to_string()
            else:
                self.__ejecuted = False
                self.create_object_excercise()

    def create_object_excercise(self):
        ejercicio_1_1_afn = Ejercicio_1_1_afn()
        ejercicio_1_1_afn.program_ejecuting()

    def go_to_status_0(self):
        self.__status = STATUS_0
        return STATUS_OUTPUT.format(self.__status)

    def go_to_status_1(self):
        self.__status = STATUS_1
        return STATUS_OUTPUT.format(self.__status)

    def go_to_status_2(self):
        self.__status = STATUS_2
        return STATUS_OUTPUT.format(self.__status)

ejercicio_1_1_afn = Ejercicio_1_1_afn()
ejercicio_1_1_afn.program_ejecuting()