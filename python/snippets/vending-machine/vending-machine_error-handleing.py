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


# Function to display the sub menu
def get_menu_sub(choice):
    sub_items = inventory[choice]
    menu_sub = ["------", f"\tThis is our {choice.capitalize()}-menu selection:"]
    for option, item in sub_items.items():
        menu_sub.append(f"\t{option} - {item}")
    menu_sub.append("\t?: ")
    return "\n".join(menu_sub)


# Function to get the quantity and verify it's an integer
def get_quantity():
    while True:
        quantity = input("\tHow many would you like?: ")
        try:
            quantity = int(quantity)
            if quantity > 0:
                return quantity
            else:
                raise ValueError("Quantity must be a positive integer")
        except ValueError as e:
            print("Invalid input! Please enter a positive integer.")
            print(e)


def verify(choice, inventory):
    while True:
        try:
            choice = int(choice)
            # Check if the uer's input is within range
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


# Function to verify the sub menu choice
def verify_sub(choice, sub_items):
    while True:
        try:
            if choice in sub_items:
                return sub_items[choice]
            else:
                raise ValueError("Invalid choice")
        except ValueError as e:
            print("You pressed the wrong button! Please try again.")
            print(e)
            choice = input("?: ")


# Function to handle the vending machine process
#def vending_machine(choice, quantity=None):
#def vending_machine(item, quantity=0):
def vending_machine():
    print(f"\n\tSorry, we're currently out items from section: {item}. \n\tApologies for the inconvenience.")
    choice_main = verify(input(get_menu_main(inventory)), list(inventory.keys()))
    choice_sub = verify_sub(input(get_menu_sub(choice_main)), inventory[choice_main])
    quantity = get_quantity()
    print("\nThank you for your order!")
    print(f"You ordered {quantity} {inventory[choice_main][choice_sub]}")


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
    #vending_machine(choice, quantity)

    menu_sub = input( get_menu_sub(choice) )
    menu_sub = verify_sub( choice, menu_sub )

    quantity = get_quantity()
# Excecute code
main()