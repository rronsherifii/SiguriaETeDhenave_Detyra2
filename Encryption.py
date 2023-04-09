import secrets
import string

from pip._vendor.pyparsing import Char


class Encryption:

    def __init__(self, gjatesia):
        self.gjatesia = gjatesia
        self.message = ''
        self.encrypted_message = ''
        self.__key = ''

    def generate_string_seed(self):
        alphabet = string.ascii_letters + string.digits
        seed = ''.join(secrets.choice(alphabet) for i in range(self.gjatesia))
        return seed

    def setMessage(self, message):
        self.message = message

    @staticmethod
    def xor(a, b):
        if a == '1' and b == '1':
            return '0'
        elif a == '1' and b == '0':
            return '1'
        elif a == '0' and b == '1':
            return '1'
        elif a == '0' and b == '0':
            return '0'

    @staticmethod
    def binary_to_decimal(binary_string):
        decimal_value = 0
        binary_string = str(binary_string)
        for digit in binary_string:
            decimal_value = decimal_value * 2 + int(digit)
        return decimal_value

    @staticmethod
    def decimal_to_binary_number(decimal_num):
        binary_num = bin(decimal_num)
        # bin() returns a string with '0b' prefix, so we slice it off using [2:]
        return binary_num[2:]

    @staticmethod
    def plain_to_number(plaintext):
        number_message = list()
        for i in range(0, len(plaintext)):
            number_message.append(ord(plaintext[i]))
        return number_message

    @staticmethod
    def num_to_binaryFormat(numList):
        for i in range(0, len(numList)):
            numList[i] = Encryption.decimal_to_binary_number(numList[i])
            difference = 8 - len(numList[i])
            if(difference > 0):
                numList[i] = '0'*difference + numList[i]
            else:
                pass


        return numList

    @staticmethod
    def key_lengthAs_plaintext(key, binaryNum):
        #
        number_key = Encryption.plain_to_number(key)
        print(number_key)
        binaryKey = list()
        #numer 576710450876
        for i in range(0,len(binaryNum)):
            binaryMember = Encryption.decimal_to_binary_number(number_key[i])
            difference = 8 - len(binaryMember)
            if(difference > 0):
                binaryKey.append('0'*difference + binaryMember)
            else:
                binaryKey.append(binaryMember)

        return binaryKey

    def xor_binary(list1, list2):
        # list 1 = mesazhi biar
        # list 2 = celesi binar

        crypted_list = list()
        crypted_binary = list()


        for i in range(0, len(list1)):
            crypted_list = [Encryption.xor(a, b) for a, b in zip(list1[i], list2[i])]
            member = ''.join(crypted_list)

            crypted_binary.append(member)

        return crypted_binary

    @staticmethod
    def numbers_to_text(lista):
        # se pari marrim mesazhin binar cipher dhe e shendrrojme ne decimal
        cipherDecimal = list()
        cipherText = list()
        for i in range(0, len(lista)):
            member = Encryption.binary_to_decimal(lista[i])
            cipherDecimal.append(member)
        print("Cipher nga binar ne decimal eshte: ", cipherDecimal)
        # tash e shendrrojme nga numri decimal ne tekst
        for j in cipherDecimal:
            cipherText.append(chr(j))

        print("Cipher nga decimal ne tekst eshte: ", cipherText)
        return ''.join(cipherText)

    def encrypt(self):
        self.__key = Encryption.generate_string_seed(self)
        print("The key is generated from a int32, and it is: ", self.__key)

        plain_number = Encryption.plain_to_number(self.message)
        print("Mesazhi i shnderruar nga shkronjat ne numra eshte: ", plain_number)

        binary_number = Encryption.num_to_binaryFormat(plain_number)
        print("Mesazhi i shendrruar nga numrat decimal ne numra binare eshte: ", binary_number)

        binary_key = Encryption.key_lengthAs_plaintext(self.__key, binary_number)
        print("Celesi i shendrruar ne te njejten gjatesi sa mesazhi dhe ne formatin binar eshte: ", binary_key)

        binary_cipher = Encryption.xor_binary(binary_number, binary_key)
        print("Cipher ne binar pasi eshte bere xor celesi me mesazhin eshte: ", binary_cipher)

        self.encrypted_message = Encryption.numbers_to_text(binary_cipher)
        print("The ciphertext that Bob reads is: ", self.encrypted_message)
        return self.encrypted_message


enc = Encryption(20)
enc.setMessage("Hello there")
enc.encrypt()

