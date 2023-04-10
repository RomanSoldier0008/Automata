class String_calculator:

    def __init__(self):
        self.__string = ""
        self.__multiply_numbers = 1
        self.__total = 0

    def get_string(self):
        return self.__string

    def set_string(self, string_value):
        self.__string = string_value

    def solve(self):
        string_one = self.__string.split("+")
        string_two = ""
        for i in range(0, len(string_one)):
            if "*" in string_one[i]:
                if string_one[i].isdigit():
                    self.__total += int(string_one[i])
                else:
                    string_two += string_one[i]
                    string_two = string_two.split("*")
                    for number in string_two:
                        self.__multiply_numbers *= int(number)
            else:
                self.__total += int(string_one[i])

    def return_output(self):
        if self.__multiply_numbers != 1:
            return self.__total + self.__multiply_numbers
        return self.__total

    def print(self):
        print(self.return_output())