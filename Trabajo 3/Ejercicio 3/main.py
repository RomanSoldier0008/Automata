from constant import *
from ipaddress import IPv4Address, AddressValueError

class Excersice_c:
    def __init__(self, adress_value=""):
        self.__adress = adress_value

    def add_ipv4(self):
        self.__adress = str(input(ADD_IPV4_INPUT))

    def is_valid_ipv4_address(self):
        try:
            IPv4Address(self.__adress)
            return True
        except AddressValueError:
            return False

    def get_out_put(self):
        if self.is_valid_ipv4_address():
            self.print(IPV4_VALID_OUTPUT.format(self.__adress))
        else:
            self.print(IPV4_NOT_VALID_OUTPUT.format(self.__adress))

    def print(self, value):
        print(value)

excersice_c = Excersice_c()
excersice_c.add_ipv4()
excersice_c.get_out_put()