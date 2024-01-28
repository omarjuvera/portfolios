# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 21:47:32 2024

@author: Omar Juvera
"""

# Main-menu items
def menuMain():
    menu: str = "------"
    menu = menu + "\n" + "1 - Cold Drinks "
    menu = menu + "\n" + "2 - Hot Drinks"
    menu = menu + "\n" + "3 - Food"
    menu = menu + "\n" + "4 - Snacks"
    menu = menu + "\n" + "?: "
    return menu

# Cold-menu items
def menuCold():
    menu: str = "------"
    menu = menu + "\n\t" + "This is our cold-menu selection:"
    menu = menu + "\n\t" + "a - Tea"
    menu = menu + "\n\t" + "b - Coke"
    menu = menu + "\n\t" + "c - 7Up"
    menu = menu + "\n\t" + "d - Milk"
    menu = menu + "\n\t" + "?: "
    return menu

# Hot-menu items
def menuHot():
    menu: str = "------"
    menu = menu + "\n\t" + "This is our hot-menu selection:"
    menu = menu + "\n\t" + "a - Tea"
    menu = menu + "\n\t" + "b - Cocoa"
    menu = menu + "\n\t" + "c - Coffee"
    menu = menu + "\n\t" + "d - Onion Soup"
    menu = menu + "\n\t" + "?: "
    return menu

# Food-menu items
def menuFood():
    menu: str = "------"
    menu = menu + "\n\t" + "This is our food-menu selection:"
    menu = menu + "\n\t" + "a - Sandwich"
    menu = menu + "\n\t" + "b - Salad"
    menu = menu + "\n\t" + "c - Chicken Soup"
    menu = menu + "\n\t" + "d - All-Organic lunch"
    menu = menu + "\n\t" + "?: "
    return menu

# Snacks-menu items
def menuSnacks():
    menu: str = "------"
    menu = menu + "\n\t" + "This is our snacks-menu selection:"
    menu = menu + "\n\t" + "a - Chocolat Bar"
    menu = menu + "\n\t" + "b - Cookies"
    menu = menu + "\n\t" + "c - Chips"
    menu = menu + "\n\t" + "d - All-Organic Healthy Snak"
    menu = menu + "\n\t" + "?: "
    return menu

def vendingMachine(menu, choice, quantity):
    # Vending Machine Inventory
    # This will be a good case for a tuple (array)
    inventoryColdA = "Tea"
    inventoryColdB = "Coke"
    inventoryColdC = "7Up"
    inventoryColdD = "Milk"
    inventoryHotA = "Tea"
    inventoryHotB = "Cocoa"
    inventoryHotC = "Coffee"
    inventoryHotD = "Onion Soup"
    inventoryFoodA = "Sandwich"
    inventoryFoodB = "Salad"
    inventoryFoodC = "Chicken Soup"
    inventoryFoodD = "All-Organic lunch"
    inventorySnacksA = "Chocolat Bar"
    inventorySnacksB = "Cookies"
    inventorySnacksC = "Chips"
    inventorySnacksD = "All-Organic Healthy Snak"

    # Display the item ordered and how many
    if menu == "cold":
        if choice == "a": print("Your order is", quantity, inventoryColdA)
        elif choice == "b": print("Your order is", quantity, inventoryColdB)
        elif choice == "c": print("Your order is", quantity, inventoryColdC)
        elif choice == "d": print("Your order is", quantity, inventoryColdD)
    elif menu == "hot":
        if choice == "a": print("Your order is", quantity, inventoryHotA)
        elif choice == "b": print("Your order is", quantity, inventoryHotB)
        elif choice == "c": print("Your order is", quantity, inventoryHotC)
        elif choice == "d": print("Your order is", quantity, inventoryHotD)
    elif menu == "food":
        if choice == "a": print("Your order is", quantity, inventoryFoodA)
        elif choice == "b": print("Your order is", quantity, inventoryFoodB)
        elif choice == "c": print("Your order is", quantity, inventoryFoodC)
        elif choice == "d": print("Your order is", quantity, inventoryFoodD)
    elif menu == "snacks":
        if choice == "a": print("Your order is", quantity, inventorySnacksA)
        elif choice == "b": print("Your order is", quantity, inventorySnacksB)
        elif choice == "c": print("Your order is", quantity, inventorySnacksC)
        elif choice == "d": print("Your order is", quantity, inventorySnacksD)

"""
def vendingMachineTuple(menu, choice):
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
    
    menu = 'cold'
    choice = 'a'
    item = inventory[menu][id]
    print(item)  # Output: Tea
"""

# Needs no introduction
def main():
    msg: str = "Welcome to SMC Python vending machine. Press a the corresponding number botton to order"
    msgQty: str = "\t" + "How many would you like?: "
    menu: str = ""
    choice: str = ""
    quantity: str = ""

    # Output main menu
    print(msg)
    menu = input( menuMain() )

    # Output sub menu
    if menu == "1":
        menu = "cold"
        choice = input( menuCold() )
        quantity = input(msgQty)
    elif menu == "2":
        menu = "hot"
        choice = input( menuHot() )
        quantity = input(msgQty)
    elif menu == "3":
        menu = "food"
        choice = input( menuFood() )
        quantity = input(msgQty)
    elif menu == "4":
        menu = "snacks"
        choice = input( menuSnacks() )
        quantity = input(msgQty)

    # Dispense the order to the vending machine
    choice = choice.lower()
    vendingMachine(menu, choice, quantity)

# Excecute code
main()