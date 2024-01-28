# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 2024

@author: Omar Juvera

Will addopt PEP 8 recommendaitons: https://peps.python.org/pep-0008/#function-and-variable-names
    Function names should be lowercase, with words separated by underscores as necessary to improve readability.
"""

import random
# Global variable to store the key
key = 0

def cipher_key():
    global key
    key = random.randint(1, 26)

def verify_key():
    global key
    if key == 0: cipher_key()

# Optimized cipher function. The result of my extracurricular 😎
# Minimal code and memory optimized. [varString += ...] has a hevier memory load according to my research
def cipher(plain_text):
    global key
    cipher_text = []

    # Modaularity: check if global key has been defined
    verify_key()

    # encode the plain text
    for text in plain_text:
        cipher_text.append(chr(ord(text) + key))

    # return the cipher text (encoded)
    return ''.join( cipher_text )

# Borring cipher function without lists
# I am including the code to demonstrate I know how to do it wihout lists
# I've shown this in the discussion #8 afterall
'''
def cipher(plain_text):
    global key
    cipher_text = ""

    # Modaularity: check if global key has been defined
    verify_key()

    for text in plain_text:
        cipherChar = chr(ord(text) + key)
        cipher_text += cipherChar

    return cipher_text
'''

def decipher(cipher_text):
    global key
    plain_text = []

    # Modaularity: check if global key has been defined
    verify_key()

    for text in cipher_text:
        plain_text.append( chr( ord(text) - key ) )

    # return the plain text (decoded)
    return ''.join( plain_text )


def main():
    global key
    cipher_text = ""
    decrypted_text = ""
    plain_text = input("What would you like to cipher-encode?: ")

    # Define key
    cipher_key()
    # Encript plain text
    cipher_text = cipher(plain_text)
    # Decypt cipher
    decrypted_text = decipher(cipher_text)
    print(f"Your Cipher is: {cipher_text}")
    print(f"Your decripted cipher for [{plain_text}] is: {decrypted_text}")

    # Check if the deciphered string matches the original string
    print("\n\t===== Verification Test =====")
    if plain_text == decrypted_text:
        print("\tSuccesful Decription!\n\tThe deciphered text matches the plain text.")
    else:
        print("\tError!\n\tThe deciphered text matches does not mach the plain text. Unable to decrypt.")

# Execute the main function
main()