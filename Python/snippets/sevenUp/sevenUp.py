# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 20:39:19 2024

@author: omarj
@author: Omar Juvera
"""

# Set variables
seven: int = 0
up: int = 0
msg: str = ""

print("To try an alternative way to do 8, Will need 2 numbers:")

# Check user input
# Feel free to type anything other than an int, like letters 😂
def validate(var):
    if var.isdigit():
        return int(var)
    else:
        print("Please enter a valid integer.")
        return inquire(msg="Retry: ")

# Get user input
def inquire(msg):
    var = input(msg)
    return validate(var)

# Dr. Pepper Factory
def sodaFactory():
    # Soda!
    if seven + up == 8:
        print("Chilling 7up! This is an alternate way to do 8 👍")
    # Still warm 😥. Needs more ice
    else:
        print("You did not get an 8. Try again")

# Get user input: first number
seven = inquire(msg="Provide the first number ")

# Get user input: second number
up = inquire(msg="Provide the second number ")

# Call the Dr. Pepper Factory
# Let's pop the soda open
sodaFactory()
