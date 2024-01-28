# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 20:40:32 2024

@author: Omar Juvera
"""

#I am gamifiying this disscussion by making a cipher snippet
#This snippet will print the words in reverse (word cipher) and change the casing to uppercase
#Since string variables are arrays, I can use the len function as well as the loop to accomplish the task.
#Bonus game: Can you spot another string function I did not mention?



def ReverseCipher(plainText):
    plainText = plainText.replace(" ", "").upper()
    cipherSize = len(plainText)
    encodedCipher = ""

    objRange = range(cipherSize, 0, -1)
    for index in objRange :
        encodedCipher += plainText[index-1]
    return encodedCipher

def main():
    cipher: str = ""
    plainText = input("What would would you like to cipher-encode?: ")

    cipher = ReverseCipher(plainText)
    print(f"Your reverse cipher for [{plainText}] is the following: {cipher}")

main()