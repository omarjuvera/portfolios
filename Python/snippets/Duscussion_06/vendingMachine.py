# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def menuMain(inventory):
    n: int = 0
    menu: str = "------"

    # Generate the menu
    while n < len(inventory):
        menu += "\n\t" + str(n+1) + " - " + inventory[n]
        n += 1
    # Add a final touch to the menu & return it
    menu += "\n\t" + "?: "
    return menu

def vendingMachine(action, index=None):
    inventory = ("Tea", "Coke", "7Up", "Milk")

    # Get main menu
    if action == "menu":
        return menuMain(inventory)
    # Get menu item
    elif action == "inventory": 
        index = int(index)-1
        return inventory[index]


# Needs no introduction
def main():
    msg: str = "Welcome to SMC Python vending machine. Press a the corresponding number botton to order"
    msgQty: str = "\t" + "How many would you like?: "
    menu: str = ""
    choice: str = ""
    quantity: str = ""

    # Vending machne is powering on
    print(msg)

    # Output main menu
    menu = vendingMachine("menu")

    
    # Get item of choice
    choice = input( menu )
    #choice = int(choice)
    choice = vendingMachine("inventory", choice)

    # Get amount ordered
    quantity = input( msgQty )

    # Dispense the order to the vending machine
    print("You ordered", quantity, choice)

# Excecute code
main()