# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

inventory = (
    ('Cold Drinks', ('Tea', 'Coke', '7Up', 'Milk')),
    ('Hot Drinks', ('Tea', 'Cocoa', 'Coffee', 'Onion Soup', 'Corn Soup')),
    ('Food', ('Sandwich', 'Salad', 'Chicken Soup', 'All-Organic lunch')),
    ('Snacks', ('Chocolat Bar', 'Cookies', 'Chips', 'All-Organic Healthy Snak'))
)

def menu_main(inventory):
    menu = "------"

    for category_index, (category_name, items) in enumerate(inventory, start=1):
        menu += f"\n{category_index}. {category_name} Menu:"
        for item_index, item in enumerate(items, start=1):
            menu += f"\n\t{item_index} - {item}"

    menu += "\n\t?: "
    return menu

# Example usage:
menu = menu_main(inventory)
print(menu)
