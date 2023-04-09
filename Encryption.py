import secrets
import string


class Encryption:

    def generate_string_seed(self, gjatesia):
        alphabet = string.ascii_letters + string.digits
        seed = ''.join(secrets.choice(alphabet) for i in range(gjatesia)).upper()
        return seed

    def xor(self,a, b):
        if a == '1' and b == '1':
            return '0'
        elif a == '1' and b == '0':
            return '1'
        elif a == '0' and b == '1':
            return '1'
        elif a == '0' and b == '0':
            return '0'
    def binary_to_decimal(binary_string):
        decimal_value = 0
        binary_string = str(binary_string)
        for digit in binary_string:
            decimal_value = decimal_value * 2 + int(digit)
        return decimal_value


    def decimal_to_binary(decimal_num):
        binary_num = bin(decimal_num)
        # bin() returns a string with '0b' prefix, so we slice it off using [2:]
        return binary_num[2:]
