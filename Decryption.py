from operation import Operations

class Decryption:
    def __init__(self):
        self.__key = ''
        self.ciphertext = ''
        self.plaintext = ''

    def set_key(self, key):
        self.__key = key

    def set_ciphertext(self, ciphertext):
        self.ciphertext = ciphertext

    def get_plaintext(self):
        return self.plaintext

    def decrypt(self):

        cipher_number = Operations.plaintext_to_number(self.ciphertext)
        print("Ciphertext i shendrruar ne ekuivalentet numra te ASCII: ", cipher_number)

        cipher_binary = Operations.number_to_binary_format(cipher_number)
        print("Ciphertext i shendrruar ne ekuivalentet binare: ", cipher_binary)

        key_binary = Operations.key_length_as_plaintext(self.__key, cipher_binary)
        print("Celesi ne binar : ", key_binary)

        plain_binary_xor = Operations.xor_binary(key_binary, cipher_binary)
        print("Plaintext ne binar: ", plain_binary_xor)

        plaintext = Operations.numbers_to_plaintext(plain_binary_xor)
        print("Plaintext : ", plaintext)

        return plaintext
