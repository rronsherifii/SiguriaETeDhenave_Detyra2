
class Operations:

    # Ben a ^ b
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

    # Bitwise XOR mes message dhe password
    @staticmethod
    def xor_binary(message_list, password_list):
        crypted_binary = list()

        for i in range(0, len(message_list)):
            crypted_list = [Operations.xor(a, b) for a, b in zip(message_list[i], password_list[i])]
            member = ''.join(crypted_list)
            crypted_binary.append(member)

        return crypted_binary

    # Kthen numrin binar ne numer decimal, duke perdorur shumezimin e fuqive te 2shit
    @staticmethod
    def binary_to_decimal(binary_string):
        decimal_value = 0
        binary_string = str(binary_string)

        binary_string = binary_string[::-1] # e kthen string mbrapsht

        for i in range(0, len(binary_string)):
            decimal_value += int(binary_string[i]) * (2 ** i)

        return decimal_value

    # Kthen numrin decimal ne numer binar
    @staticmethod
    def decimal_to_binary(decimal_num):
        binary_num = bin(decimal_num)
        # bin() returns a string with '0b' prefix, so we slice it off using [2:]
        return binary_num[2:]

    # E kthen plaintext ne nje array te karaktereve me numer
    @staticmethod
    def plaintext_to_number(plaintext):
        number_message = list()
        for i in range(0, len(plaintext)):
            number_message.append(ord(plaintext[i]))
        return number_message

    @staticmethod
    def numbers_to_plaintext(lista):
        # se pari marrim mesazhin binar cipher dhe e shendrrojme ne decimal
        cipherDecimal = list()
        cipherText = list()
        for i in range(0, len(lista)):
            member = Operations.binary_to_decimal(lista[i])
            cipherDecimal.append(member)
        # print("Cipher nga binar ne decimal eshte: ", cipherDecimal)

        # tash e shendrrojme nga numri decimal ne tekst
        for j in cipherDecimal:
            cipherText.append(chr(j))

        # print("Cipher nga decimal ne tekst eshte: ", cipherText)
        return ''.join(cipherText)

    # Listen e numrave e kthen ne ekuivalentin binar
    @staticmethod
    def number_to_binary_format(num_list):
        for i in range(0, len(num_list)):
            num_list[i] = Operations.decimal_to_binary(num_list[i])
            num_list[i] = Operations.binary_to_eight(num_list[i])
        return num_list

    # Passwordin e bejme slice ashtu qe te jete kompatibil me plaintext
    @staticmethod
    def key_length_as_plaintext(key, binary_num):
        number_key = Operations.plaintext_to_number(key)
        binary_key = list()

        for i in range(0, len(binary_num)):
            binary_member = Operations.decimal_to_binary(number_key[i])
            binary_key.append(Operations.binary_to_eight(binary_member))

        return binary_key

    # Kontrollon gjatesine numrin binar dhe i shton 0 si padding per tu bere 8 shifra
    @staticmethod
    def binary_to_eight(number):
        difference = 8 - len(number)
        result = ''
        if difference > 0:
            result = '0'*difference + number
        else:
            result = number

        return result

