from random import randint
import sys


# def generator(g, x, p):
#     return pow(g, x) % p


# def encrypt(plaintext, key):
#     cipher = []
#     for char in plaintext:
#         cipher.append(((ord(char) * key*311)))
#     return cipher


# def is_prime(p):
#     v = 0
#     for i in range(2, p + 1):
#         if p % i == 0:
#             v = v + 1
#     if v > 1:
#         return False
#     else:
#         return True


# def dynamic_xor_encrypt(plaintext, text_key):
#     cipher_text = ""
#     key_length = len(text_key)
#     for i, char in enumerate(plaintext[::-1]):
#         key_char = text_key[i % key_length]
#         encrypted_char = chr(ord(char) ^ ord(key_char))
#         cipher_text += encrypted_char
#     return cipher_text


# def test(plain_text, text_key):
#     p = 97
#     g = 31
#     if not is_prime(p) and not is_prime(g):
#         print("Enter prime numbers")
#         return
#     a = randint(p-10, p)
#     b = randint(g-10, g)
#     print(f"a = {a}")
#     print(f"b = {b}")
#     u = generator(g, a, p)
#     v = generator(g, b, p)
#     key = generator(v, a, p)
#     b_key = generator(u, b, p)
#     shared_key = None
#     if key == b_key:
#         shared_key = key
#     else:
#         print("Invalid key")
#         return
#     semi_cipher = dynamic_xor_encrypt(plain_text, text_key)
#     cipher = encrypt(semi_cipher, shared_key)
#     print(f'cipher is: {cipher}')

p = 97
g = 31
a = 88
b = 26
cipher = [97965, 185045, 740180, 946995, 1012305, 21770, 827260, 751065, 718410, 457170, 0, 903455, 228585, 54425, 740180, 0, 239470,
          936110, 10885, 674870, 261240, 293895, 65310, 65310, 185045, 65310, 283010, 555135, 348320, 533365, 283010, 76195, 130620, 185045]


def generator(g, x, p):
    return pow(g, x) % p


def decrypt(encryptedText, key):
    return [chr(each // (key * 311)) for each in encryptedText]


def dynamic_xor_decrypt(encrypted_text, text_key):
    plain_text = ""
    key_length = len(text_key)
    for i, each in enumerate(encrypted_text):
        key_char = text_key[i % key_length]
        plain_text += chr(ord(each) ^ ord(key_char))
    return plain_text[::-1]


u = generator(g, a, p)
v = generator(g, b, p)
key = generator(v, a, p)
b_key = generator(u, b, p)
shared_key = None

if key == b_key:
    shared_key = key
else:
    print("Invalid key")

semi_cipher = decrypt(cipher, shared_key)
plain_text = dynamic_xor_decrypt(semi_cipher, "trudeau")
print(plain_text)

