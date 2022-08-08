# 1
import hashlib

cipher = {'p': 'o', 'y': 'h', 't': 'n',
          'h': 't', 'o': 'y', 'n': 'p', 'a': 'c', 'b': 'd'}
print(cipher)


def encrypt(cipher, word):
    encrypted = ""
    for char in word:
        if char not in cipher:
            encrypted += char
        else:
            encrypted += cipher[char]
    return encrypted


def toHash(word):
    word = word.encode()
    hashed_enword = hashlib.sha256(word).hexdigest()
    return hashed_enword


def addNewEncrypted(word):
    word1 = encrypt(cipher, word)
    word2 = toHash(word1)
    return word1, word2, word


word = input("Введите значения для шифрования: ")
enword = addNewEncrypted(word)
print(enword)

print(cipher.get('3423', "1000"))
