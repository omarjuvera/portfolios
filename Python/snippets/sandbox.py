# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


def reverse_cipher(plain_text):
    encoded_cipher = []
    # Removing spaces and converting to uppercase in one step
    # If the user presses enter without providing any value, encoded_cipher is already initialized as an empty string without explicit assignment. No need for [encoded_cipher = ""]
    plain_text = plain_text.replace(" ", "").upper()

    for char in reversed(plain_text):
        encoded_cipher.append( char )

    return "".join(encoded_cipher)

def main():
    cipher = ""
    # If the user presses enter without providing any value, input already initializes plain_text as an empty string without explicit assignment. No need for [plain_text = ""]
    plain_text = input("What would you like to cipher-encode?: ")

    cipher = reverse_cipher(plain_text)
    print(f"Your reverse cipher for [{plain_text}] is the following: {cipher}")

main()