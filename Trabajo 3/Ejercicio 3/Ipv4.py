class Ipv4:
    def __init__(self):
        self.__ipv4 = ""

    def set_ipv4(self, ipv4):
        self.__ipv4 = ipv4

    def user_enter_ipv4(self):
        self.set_ipv4(str(input("Ingrese IPV4: ")))

    def verify_is_ipv4(self):
        try:
            count_point_in_string = self.__ipv4.count(".")
            if count_point_in_string == 3:
                self.__ipv4 = self.__ipv4.split(".")
                count = 0
                for i in range(0, len(self.__ipv4)):
                    container = self.__ipv4[i]
                    container = int(container)
                    if 255 >= container >= 0:
                        count += 1
                        if count >= 4:
                            return True
            return False
        except ValueError:
            return False


ipv4 = Ipv4()
ipv4.user_enter_ipv4()
print(ipv4.verify_is_ipv4())