import secrets
import string
from operation import Operations


class Encryption:

    def __init__(self, gjatesia):
        self.gjatesia = gjatesia
        self.message = ''
        self.encrypted_message = ''
        self.__key = self.generate_string_seed()

    def generate_string_seed(self):
        alphabet = string.ascii_letters + string.digits
        seed = ''.join(secrets.choice(alphabet) for i in range(self.gjatesia))
        return seed

    def set_message(self, message):
        self.message = message

    def get_encrypted_message(self):
        return self.encrypted_message

    def encrypt(self):
        print("The key is generated from a int32, and it is: ", self.__key)

        plain_number = Operations.plaintext_to_number(self.message)
        print("Mesazhi i shnderruar nga shkronjat ne numra eshte: ", plain_number)

        binary_number = Operations.number_to_binary_format(plain_number)
        print("Mesazhi i shendrruar nga numrat decimal ne numra binare eshte: ", binary_number)

        binary_key = Operations.key_length_as_plaintext(self.__key, binary_number)
        print("Celesi i shendrruar ne te njejten gjatesi sa mesazhi dhe ne formatin binar eshte: ", binary_key)

        binary_cipher = Operations.xor_binary(binary_number, binary_key)
        print("Cipher ne binar pasi eshte bere xor celesi me mesazhin eshte: ", binary_cipher)

        self.encrypted_message = Operations.numbers_to_plaintext(binary_cipher)
        print("The ciphertext that Bob reads is: ", self.encrypted_message)

        return self.encrypted_message

