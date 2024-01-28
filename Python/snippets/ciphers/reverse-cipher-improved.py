# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 01:39:06 2024

@author: Omar Juvera
"""

def ReverseCipher(plainText):
    plainText = plainText.replace(" ", "").upper()
    encodedCipher = []

    for char in reversed(plainText):
        encodedCipher.append(char)

    return ''.join(encodedCipher)

def main():
    cipher = ""
    plainText = input("What would you like to cipher-encode?: ")

    cipher = ReverseCipher(plainText)
    print(f"Your reverse cipher for [{plainText}] is the following: {cipher}")

main()
