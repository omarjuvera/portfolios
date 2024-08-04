def menuMain():
    menu: str = "------"
    menu = menu + "\n" + "1 - Cold Drinks "
    menu = menu + "\n" + "2 - Hot Drinks"
    menu = menu + "\n" + "3 - Food"
    menu = menu + "\n" + "4 - Snacks"
    menu = menu + "\n" + "?: "

    menu = input(menu)
    menu = verify("main", menu)

def menuCold():
    menu: str = "------"
    menu = menu + "\n\t" + "This is our cold-menu selection:"
    menu = menu + "\n\t" + "a - Tea"
    menu = menu + "\n\t" + "b - Coke"
    menu = menu + "\n\t" + "c - 7Up"
    menu = menu + "\n\t" + "d - Milk"
    menu = menu + "\n\t" + "x - Return"
    menu = menu + "\n\t" + "?: "

    menu = input(menu)
    menu = verify("cold", menu)

def menuHot():
    menu: str = "------"
    menu = menu + "\n\t" + "This is our hot-menu selection:"
    menu = menu + "\n\t" + "a - Tea"
    menu = menu + "\n\t" + "b - Cocoa"
    menu = menu + "\n\t" + "c - Coffee"
    menu = menu + "\n\t" + "d - Onion Soup"
    menu = menu + "\n\t" + "e - Corn Soup"
    menu = menu + "\n\t" + "x - Return"
    menu = menu + "\n\t" + "?: "

    menu = input(menu)
    menu = verify("hot", menu)

def menuFood():
    menu: str = "------"
    menu = menu + "\n\t" + "This is our cold-menu selection:"
    menu = menu + "\n\t" + "a - Sandwich"
    menu = menu + "\n\t" + "b - Salad"
    menu = menu + "\n\t" + "c - Chicken Soup"
    menu = menu + "\n\t" + "d - All-Organic lunch"
    menu = menu + "\n\t" + "x - Return"
    menu = menu + "\n\t" + "?: "

    menu = input(menu)
    menu = verify("food", menu)

def menuSnacks():
    menu: str = "------"
    menu = menu + "\n\t" + "This is our cold-menu selection:"
    menu = menu + "\n\t" + "a - Chocolat Bar"
    menu = menu + "\n\t" + "b - Cookies"
    menu = menu + "\n\t" + "c - Chips"
    menu = menu + "\n\t" + "d - All-Organic Healthy Snak"
    menu = menu + "\n\t" + "x - Return"
    menu = menu + "\n\t" + "?: "

    menu = input(menu)
    menu = verify("snacks", menu)

def verify(source, choice):
    msg: str = "You pressed the wrong button. Please try again"

    if source != "main":
        if choice == "x": 
            return menuMain()
        elif choice == "a" or choice == "b" or choice == "c" or choice == "d": 
            return choice
        # any other entry must be either "main" or incorrect

        return choice

    menu = choice
    if source == "main":
        if menu == "1" or menu == "2" or menu == "3" or menu == "4": return choice
        
    elif source == "cold":
        if menu == "a" or menu == "b" or menu == "c" or menu == "d": return choice
    elif source == "hot":
        if menu == "a" or menu == "b" or menu == "c" or menu == "d" or menu == "e": return choice
    elif source == "food":
        if menu == "a" or menu == "b" or menu == "c" or menu == "d": return choice
    elif source == "snacks":
        if menu == "a" or menu == "b" or menu == "c" or menu == "d": return choice
    else:
        print(msg)
        return verify(source, menu)

def vendingMachine(menu, choice, quantity):
    menuMain = msg + "\n" + "1 - Hot Drinks "
    menuMain = msg + "\n" + "2 - Cold Drinks"
    menuMain = msg + "\n" + "3 - Food"
    menuMain = msg + "\n" + "4 - Snacks"

    # Check if user entered the correct int value
    mainMenu = input(msg)
    if choice == "1" or choice == "2" or choice == "3" or choice == "4":
        return choice
    else:
        print("Invalid choice. Please try again.")
        return invalidChoice()

# Needs no introduction
def main():
    msg: str = "Welcome to SMC Python vending machine. Press a the corresponding number botton to order"
    menu: str = ""
    choice: str = ""
    quantity: str = ""

    print(msg)
    menu = menuMain()
    #if menu == "1" or menu == "2" or menu == "3" or menu == "4":
    if menu == "1":
        choice = menuHot()
    elif menu == "2":
        choice = menuCold()
    else:
        print("You pressed the wrong button. Please try again")
        menu = menuMain()

    menu, choice, quantity = vendingMachine(menu, choice, quantity)

# Excecute code
main()