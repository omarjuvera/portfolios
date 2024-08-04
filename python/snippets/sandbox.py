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

'''
def verify(choice, inventory):
    while True:
        try:
            choice = int(choice)
            # Get the key corresponding to the user's choice
            if 1 <= choice <= len(inventory):
            # Get the key corresponding to the user's choice
                menu_main = list(inventory.keys())[choice - 1]
                return menu_main
            else:
                # Trigger the except block by setting choice to 'invalid'/a non-integer value
                # Without this else, it will loop forever, if the user enters an int outside the range of inventory (1 ~ 4)
                # choice = 'invalid'
                raise ValueError
                #raise ValueError("\nYou pressed the wrong button! Please try again.")
        #except ValueError as e:
        except ValueError:
            print("\nYou pressed the wrong button! Please try again.")
            #print(e)
            choice = input( get_menu_main(inventory) )
'''
def verify(choice, inventory):
    while True:
        try:
            choice = int(choice)
        except:
            print("\n\tYou pressed the wrong button! Please try again.")
            choice = input( get_menu_main(inventory) )

        try:
            if 1 <= choice <= len(inventory):
                # Get the key corresponding to the user's choice
                menu_main = list(inventory.keys())[choice - 1]
                return menu_main
            else:
                # Trigger the except block by raising an exception
                # Without this else condition, it will loop forever, if the user enters an int outside the range of inventory (1 ~ 4)
                raise Exception("\nYou pressed the wrong button! Please try again.")
        except:
            print("\n\tYou pressed the wrong button! Please try again.")
            choice = input( get_menu_main(inventory) )




#def vending_machine(choice, quantity=None):
def vending_machine(item):
    print(f"\n\tSorry, we're currently out items from section: {item}. \n\tApologies for the inconvenience.")


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