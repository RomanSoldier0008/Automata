import re

def check_email_internet_domain(email):
    string1 = r"([a-zA-Z0-9]|\._-])+@([a-zA-Z0-9]|\.-)+\.(com|edu|org|net|eu)(\.(us|col|mex|ar|uk))?"
    if re.fullmatch(string1, email):
        print("Your email and internet domain are correct")
    else:
        print("Please write another email and internet domain")


check_email_internet_domain("juanchoimaz20@um.edu.arr")
