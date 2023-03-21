class Calculator:
    def __init__(self, string_value):
        self.__string = string_value

    # def solve(self):

    def transform_to_int(self):
        strings_list = self.__string.split(" ")
        numbers = []
        operations = []
        total = 0
        for i in range(len(strings_list)):
            if strings_list[i].isnumeric():
                numbers.append(int(strings_list[i]))
            if strings_list[i].isascii():
                operations.append(strings_list[i])
        for i in range(len(numbers)):
            try:
                if operations[i] == "*":
                    total *= numbers[i]
                else:
                    total += numbers[i]
            except IndexError:
                print("La lista operaciones no tiene ese índice")
        return total

string = Calculator("2 * 2 * 2 + 32 * 2")
print(string.transform_to_int())