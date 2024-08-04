# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 21:30:09 2024

@author: Omar Juvera
"""

def menu_main(inventory):
    menu = "------"

    # Generate the menu
    for n, item in enumerate(inventory, start=1):
        # Convert the index to a letter using chr()
        letter = chr(ord('a') + n - 1)
        menu += f"\n\t{letter} - {item}"

    # Add a final touch to the menu & return it
    menu += "\n\t?: "
    return menu

# Example usage
inventory = ["Tea", "Coke", "7Up", "Milk"]
menu = menu_main(inventory)
print(menu)
