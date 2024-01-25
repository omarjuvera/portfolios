# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 14:31:38 2024

@author: Omar Juvera

Write the definition of a function that takes one number, that represents a temperature in Fahrenheit. The function prints the equivalent temperature in degrees Celsius. (1 point)

Write the definition of another function that takes two numbers, that represent speed in miles/hour and time in minutes. The function prints the distance traveled based on that speed and time. (1 points)

Write the definition of a function named main. It takes no input, hence empty parenthesis, and does the following:
- starts by showing on 3 lines using one print statement (you'll need to use the escape character for the new line) the following:
        Enter 1 to convert Fahrenheit temperature to Celsius
        Enter to calculate distance travelled 
        Enter 3 to exit
- uses one input statement to get which number the user wants to input (1 or 2). Call this main_input. Make sure to make main_input an integer.
-  if main_input contains 1, get one input then call the function of step 1 and pass it the input. After this line, call main. 
-  if main_input contains 2, get two more inputs and call the function of step 2 and pass it those two inputs; watch out for the order.After this line call main.
-  if main_input contains 3, then print a good bye message. Do not call main, as this will cause 'us' not to exit.
-  if main-input is none of the above, print an error message, then call main.

After you complete the definition of the function main, write a statement to call main. (3 points)
"""

# Convert to farenheits
def convertTemperture():
    # Get Fahrenheit temperature from user
    f = input("What is the temperature, in Fahrenheit? ")
    f = round(float(f), 2)

    # Convert to celcius
    c = (f - 32) * (5/9)
    c = round(float(c), 2)

    # Output
    print(f"{f:.2f}°F Fahrenheit is {c:.2f}°C celcius")


# Distance traveled
def distanceTraveled():
    # Get Speed
    s = input("What is the speed (mph)? ")
    s = round(float(s), 2)
    # Get time (in minutes)
    m = input("In how many minutes? ")
    m = round(float(m), 2)
    # Distance traveled
    d = s * (m / 60)
    d = round(float(d), 2)
    print("The total distance traveled at", s, "mph in", m, "minutes is", d, "miles")


# Check if user choice is 1, 2 or 3
def main():
    choice: int = 0
    msg = "\tEnter 1 to convert Fahrenheit temperature to Celsius"
    msg = msg + "\n\t" + "Enter to calculate distance travelled"
    msg = msg + "\n\t" + "Enter 3 to exit"
    msg = msg + "\n\t" + "1, 2, 3?: "
    # Check if user entered the correct int value
    choice = input(msg)
    if choice == "1" or choice == "2" or choice == "3":
        choice = int(choice)
        return choice
    else:
        print("=========================================")
        print("=== Invalid choice. Please try again. ===")
        print("=========================================")
        return main()

# Needs no introduction
def mainInput():
    main_input: int = 0
    main_input = mainInput()
    # Get celcius temperture from user
    if main_input == 1:
        convertTemperture()
    # Time machine
    elif main_input == 2:
        distanceTraveled()
    elif main_input == 3:
        print("Goodbye!")

# Excecute code
main()