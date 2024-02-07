# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 19:22:05 2024

@author: Omar Juvera
"""

# Inventory Menu (nested dictionary)
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


def get_menu_main(inventory):
    menu: list = ["------"]
    for option, category in enumerate(inventory, start=1):
        menu.append( f"{option} - {category.capitalize()}" )

    menu.append("?: ")
    return "\n".join(menu)


def verify(choice, inventory):
    while True:
        try:
            choice = int(choice)
            if 1 <= choice <= len(inventory):
            #if choice < 1 or choice > len(inventory):
                return list(inventory.keys())[choice - 1]
        except ValueError:
            menu: str = ""

            print("You pressed the wrong button! Please try again.")
            menu = get_menu_main(inventory)
            choice = input(menu)


#def vending_machine(choice, quantity=None):
def vending_machine(item):
    print(f"Sorry, we're currently out of {item}. Apologies for the inconvenience.")


# Needs no introduction
def main():
    msg: str = "Welcome to SMC Python vending machine. Press a the corresponding botton to order"
    menu: str = ""
    choice: str = ""
    quantity: str = ""
    global inventory

    print(msg)
    menu = get_menu_main(inventory)
    choice = input(menu)
    
    choice = verify(choice, inventory)
    vending_machine(choice)

# Excecute code
main()