# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 21:56:15 2024

@author: Omar Juvera
"""

def menu_main(inventory):
    menu = "------"

    # Generate the menu
    for category, items in inventory.items():
        menu += f"\n{category.capitalize()}"
        for index, item in enumerate(items, start=1):
            menu += f"\n\t{index} - {items[item]}"

    # Add a final touch to the menu & return it
    menu += "\n\t?: "
    return menu

# Example usage:
inventory = {
    'cold': {
        'a': "Tea",
        'b': "Coke",
        'c': "7Up",
        'd': "Milk",
    },
    'hot': {
        'a': "Tea",
        'b': "Cocoa",
        'c': "Coffee",
        'd': "Onion Soup",
        'e': "Corn Soup",
    },
    'food': {
        'a': "Sandwich",
        'b': "Salad",
        'c': "Chicken Soup",
        'd': "All-Organic lunch",
    },
    'snacks': {
        'a': "Chocolat Bar",
        'b': "Cookies",
        'c': "Chips",
        'd': "All-Organic Healthy Snak",
    }
}

menu = menu_main(inventory)
print(menu)
