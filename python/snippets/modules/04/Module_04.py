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
    f: float = 0.00
    c: float = 0.00

    """    
    # Get celcius temperture from user
    c = inquire(msg="What is the temperture, in Fahrenheit? ")
    c = float(c)

    # Convert to farenheits
    f = c * (9/5)  + 32
    print(f"{c}°C celcius is {f}°F Fahrenheit")
    """

    # Get Fahrenheit temperature from user
    f = inquire("What is the temperature, in Fahrenheit? ")
    #f = round(f)

    # Convert to celcius
    c = (f - 32) * (5/9)

    # Round
    f = round(f, 2) if isinstance(f, float) else f
    c = round(c, 2) if isinstance(c, float) else c
    print(f"{f}°F Fahrenheit is {c}°C celcius")
    #else print(f"{f:,.2f}°F Fahrenheit is {c:,.2f}°C celcius")

# Distance traveled
def distanceTraveled():
    s: int = 0
    m: int = 0
    d: float = 0.0

    # Get Speed
    s = inquire("What is the speed (mph)? ")

    # Get time (in minutes)
    m = inquire("In how many minutes? ")

    # Distance traveled
    d = s * (m / 60)

    # Round
    s = round(s, 2) if isinstance(s, float) else s
    m = round(m, 2) if isinstance(m, float) else s
    d = round(d, 2) if isinstance(d, float) else d
    print("The total distance traveled at", s, "mph in", m, "minutes is", d, "miles")

# Check if user choice is 1, 2 or 3
def mainInput():
    choice: int = 0
    msg = "Enter 1 to convert Fahrenheit temperature to Celsius"
    msg = msg + "\n" + "Enter to calculate distance travelled"
    msg = msg + "\n" + "Enter 3 to exit"
    msg = msg + "\n" + "1, 2, 3?: "

    # Check if user entered the correct int value
    choice = inquire(msg, int)

    # Process selection
    if 1 <= choice <=3:
        return choice
    else:
        print("Invalid choice. Please try again.")
        return mainInput()

# Get user input
def inquire(var, varType=None):
    var = input(var)
    return validate(var, varType)

# Check if int
"""
def validate(var):
    if var.isdigit(): 
        return var
    else:
        print("Please enter a valid integer")
        return inquire(msg="Retry: ")
"""
def validate(value, valueType):
    # Make sure user enters 1~3 ONLY. Not floats - mainInput()
    if valueType == int:
        return int(value) if value.isdigit() else tryAgain(valueType)
    # Check if int
    elif value.isdigit():
        return int(value)
    # Check if float
    # multiple . are not allowed
    elif value.replace(".", "", 1).isnumeric():
        return float(value)
    else:
        return tryAgain(valueType)


def tryAgain(valType):
        print("Please enter a valid integer")
        return inquire("Retry: ", valType)

def main():
    main_input: int = 0
    main_input = mainInput()

    # Get celcius temperture from user
    if main_input == 1:
        convertTemperture()
    # Time machine
    elif main_input == 2:
        distanceTraveled()
    else:
        print("Goodbye!")


main()