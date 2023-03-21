class String_format:

    def validate_1(self, string_value):
        for letter in string_value:
            if letter.isalnum():
                return letter.isalnum()
            else:
                return False
        # ------------------------------------------------------------------------------------------------------------
    def validate_2(self, string_value):
        for letter in string_value:
            if letter.isalpha():
                return letter.isalpha()
            else:
                return False

string = String_format()
print(string.validate_1("+"))
print(string.validate_2(" "))