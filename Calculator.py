class Calculator:
    def __init__(self, string_value):
        self.__string = string_value
        self.__total = 0

    def solve(self):
        strings_list = self.__string.split(" ")
        self.__string = ""
        for letter in strings_list:
            self.__string += letter
        self.__total = eval(self.__string)
        return self.__total

string = Calculator("2 * 2 * 2 + 32 * 2")
print(string.solve())