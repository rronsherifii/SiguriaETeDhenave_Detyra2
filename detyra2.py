# # one time pad
# # 1. krijimi i celesit me int32 ose string seed
# # 2. Gjenerimi i mesazhit nga user dergues
# # 3. Perdoret alfabeti anglez me 26 shkronja secila e mapuar ne numrat 1 deri 26
# # 4. Mesazhi behet xor me celesin , celesi behet slice ashtu qe te jete i gjate sa mesazhi
# # 5. Mesazhi dergohet dhe marresi e ben xor ciphertext me celesin qe ai poashtu posedon
# # 6. Fitohet mesazhi plain
# # 7. Nese tentohet komunikimi prape celesi nderrohet, pasi eshte one time pad
# # 8. Ne kod perdoren dy funksione nje per enkriptim dhe nje per dekriptim
# import random
#
# import numpy as np
#
# # gjenerimi i celesit, i cili duhet te jete me se shumti 10 numra
# low = -2147483648
# high = 2147483647
#
#
# def generateKey():
#     tryKey = 1
#     while tryKey > 0:
#         key = np.random.randint(low, high, dtype=np.int32)
#         if key < 2000000000:
#             tryKey += 1
#         else:
#             break
#     return key
#
#
# # definimi i shkronjave dhe korrespondenteve numra te tyre
# alphabet = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6,
#             'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12,
#             'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18,
#             'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24,
#             'Y': 25, 'Z': 26}
#
#
# # funksioni per xor
# def xor(a, b):
#     if a == '1' and b == '1':
#         return '0'
#     elif a == '1' and b == '0':
#         return '1'
#     elif a == '0' and b == '1':
#         return '1'
#     elif a == '0' and b == '0':
#         return '0'
#
#
# def binary_to_decimal(binary_string):
#     decimal_value = 0
#     binary_string = str(binary_string)
#     for digit in binary_string:
#         decimal_value = decimal_value * 2 + int(digit)
#     return decimal_value
#
#
# def decimal_to_binary(decimal_num):
#     binary_num = bin(decimal_num)
#     # bin() returns a string with '0b' prefix, so we slice it off using [2:]
#     return binary_num[2:]
#
#
# # shendrrimi i mesazhit ne ekuivalentet numra
# def plain_to_number(plaintext):
#     numberMessage = list()
#     for i in range(0, len(plaintext)):
#         for j in alphabet:
#             if j == plaintext[i].upper():
#                 numberMessage.append(alphabet[j])
#     return numberMessage
#
#
#
#
# # funksioni qe shendrron cdo listen e numrave ne mesazh ne liste me numra binar
# def numToBinaryFormat(numList):
#     for i in range(0, len(numList)):
#         numList[i] = decimal_to_binary(numList[i])
#
#     return numList
#
#
#
#
# # funksioni qe kthen celesin me gjatesi te njejte sa plaintext
#
# def key_lengthAs_plaintext(key,binaryNum):
#     binaryKey = decimal_to_binary(key)
#
#     msgLength = 0
#     msgStart = 0
#
#     keyList = list()
#
#     for i in range(0, len(binaryNum)):
#         msgLength += len(binaryNum[i])
#         keyList.append(binaryKey[msgStart:msgLength])
#         msgStart = msgLength
#
#     return keyList
#
#
# # funksioni qe ben xor ne mes te dy vargjeve me numra binar. Na duhet per enkriptim si dhe dekriptim
# def xorBinary(list1, list2):
#     # vendosja e numrave binare nje nga nje duke i bere xor
#     cryptedList = list()
#     # perkthimi i kesaj liste ne formatin e duhur binar
#     cryptedBinary = list()
#     member = ''
#     starti = 0
#
#     for i in range(0, len(list1)):
#         for j in range(0, len(list1[i])):
#             cryptedList.append(xor(list1[i][j], list2[i][j]))
#             # print(xor(binaryNum[i][j], binaryKey[i][j]))
#         finish = len(list1[i]) + starti
#         # print(cryptedList[starti:finish])
#
#         member = ''.join(cryptedList[starti:finish])
#
#         starti = finish
#         cryptedBinary.append(member)
#     return cryptedBinary
#
#
#
# # shnderrimi i mesazhit binar ne mesazh plaintext
# def numbersToText(lista):
#     # se pari marrim mesazhin binar cipher dhe e shendrrojme ne decimal
#     cipherDecimal = list()
#     cipherText = list()
#     for i in range(0, len(lista)):
#         member = binary_to_decimal(lista[i])
#         cipherDecimal.append(member)
#     print("Cipher nga binar ne decimal eshte: ",cipherDecimal)
#     # tash e shendrrojme nga numri decimal ne tekst
#     for j in cipherDecimal:
#         for a in alphabet:
#             if j == alphabet[a]:
#                 cipherText.append(a)
#             elif (j > 26) and alphabet[a] == (j%26):
#                 #val = j % 26
#                 #letter = alphabet[val]
#                 cipherText.append(a)
#         if j == 0:
#             cipherText.append('Z')
#     print("Cipher nga decimal ne tekst eshte: ",cipherText)
#     return ''.join(cipherText)
#
#
# def encrypt():
#     print("\n Alice and Bob have agreed on using a new key every time they communicate!")
#     global key
#     key = generateKey()
#     print("The key is generated from a int32, and it is: ", key)
#
#     global plaintext
#     plaintext = input("Alice writes a message: ")
#
#
#     # lista qe ka numrat per cdo shkronje te mesazhit
#     plainNum = plain_to_number(plaintext)
#     print("Mesazhi i shnderruar nga shkronjat ne numra eshte: ", plainNum)
#
#
#     # lista qe ka anetaret e mesazhit ne numra binare
#     binaryNum = numToBinaryFormat(plainNum)
#     print("Mesazhi i shendrruar nga numrat decimal ne numra binare eshte: ", binaryNum)
#
#
#     # celesi nga int32 ne numer binar
#     binaryKey = key_lengthAs_plaintext(key,binaryNum)
#     print("Celesi i shendrruar ne te njejten gjatesi sa mesazhi dhe ne formatin binar eshte: ", binaryKey)
#
#
#     #Ciphertext ne format binar
#     binaryCipher = xorBinary(binaryNum, binaryKey)
#     print("Cipher ne binar pasi eshte bere xor celesi me mesazhin eshte: ", binaryCipher)
#
#
#     ciphertext = numbersToText(binaryCipher)
#     print("The ciphertext that Bob reads is: ", ciphertext)
#     return ciphertext
#
#
#
# # funksioni poshte krahason cipher gjate dekriptimit kur shendrrohet ne format binar,
# # a eshte i njejte me formatin binar te cipher gjate enkriptimit, nese jo, beji te njejta ne menyre qe
# # rezultati te jete i sakte
# def keepCipherLength(cipher1,cipher2):
#     for i in range(0,len(cipher2)):
#         if(len(cipher1[i]) != len(cipher2[i])):
#             cipher1[i] = cipher2[i]
#
#
# def decrypt(ciphertext):
#     print("Ciphertext eshte: ",ciphertext)
#     cipherNr = plain_to_number(ciphertext)
#     print("Ciphertext ne numra eshte: ",cipherNr)
#
#
#     cipher = list()
#
#     for i in range(0,len(cipherNr)):
#         if(cipherNr[i] == 26):
#             cipher.append('0000')
#         else:
#             cipher.append(decimal_to_binary(cipherNr[i]))
#
#     plainNum = plain_to_number(plaintext)
#     binaryNum = numToBinaryFormat(plainNum)
#     binaryKey = key_lengthAs_plaintext(key,binaryNum)
#     binaryCipher = xorBinary(binaryNum, binaryKey)
#
#     keepCipherLength(cipher,binaryCipher)
#     print("Cipher si string me numer: ",cipher)
#
#     print("Celesi ne binar eshte: ",binaryKey)
#     plain = xorBinary(cipher,binaryKey)
#     print("Plaintext ne binare eshte : ",plain)
#     text = numbersToText(plain)
#     print("Mesazhi plaintext eshte i dekriptuar! ",text)
#     return text
#
#
#
#
# # programi kryesor ne te cilin thirret funksionet e shkruara
# start = 1
# while start == 1:
#     # ketu thirren funksionet per enkriptim dhe dekriptim
#     # poashtu pyetet user nese deshiron te shkembeje prape mesazh, me crast nderrohet celesi
#     ans = input("\nDeshironi te komunikoni? \n")
#     if( ans == 'y' or ans =='Y'):
#         print("--------ENCRYPTION--------")
#         c = encrypt()
#         print("\n\n\n")
#         print("--------DECRYPTION--------")
#         decrypt(c)
#     elif( ans == 'n' or ans == 'N'):
#         break
#
#
#
#
#
#
#
#
