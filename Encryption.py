import secrets
import string


class Encryption:

    def generate_string_seed(self, gjatesia):
        alphabet = string.ascii_letters + string.digits
        seed = ''.join(secrets.choice(alphabet) for i in range(gjatesia)).upper()
        return seed

    def xor(self, a, b):
        if a == '1' and b == '1':
            return '0'
        elif a == '1' and b == '0':
            return '1'
        elif a == '0' and b == '1':
            return '1'
        elif a == '0' and b == '0':
            return '0'


