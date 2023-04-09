import secrets
import string


class Encryption:

    def generate_string_seed(self, gjatesia):
        alphabet = string.ascii_letters + string.digits
        seed = ''.join(secrets.choice(alphabet) for i in range(gjatesia)).upper()
        return seed

