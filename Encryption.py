import secrets
import string

from detyra2 import decimal_to_binary


class Encryption:

    @staticmethod
    def generate_string_seed(gjatesia):
        alphabet = string.ascii_letters + string.digits
        seed = ''.join(secrets.choice(alphabet) for i in range(gjatesia)).upper()
        return seed

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
    def decimal_to_binary(decimal_num):
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
            numList[i] = decimal_to_binary(numList[i])

        return numList
    @staticmethod
    def key_lengthAs_plaintext(key,binaryNum):
        binaryKey = decimal_to_binary(key)

        msgLength = 0
        msgStart = 0

        keyList = list()

        for i in range(0, len(binaryNum)):
            msgLength += len(binaryNum[i])
            keyList.append(binaryKey[msgStart:msgLength])
            msgStart = msgLength

        return keyList