# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 23:27:51 2024
@author: Omar Juvera

Write a program that calculates an employee's weekly income 
based on the number of hours worked, and their hourly pay as follows: 

    1. Ask the user to enter their name. Save this into a variable. 
    Name it properly. 

    2. Ask the user to enter their hourly rate. 
        Show them a prompt that looks like the following: 
        Sarah, what is your hourly rate? 
        Replacing Sarah for their actual no which you got in step 1. 
        Save the hourly rate in a variable and note 
        you should convert the into to a floating point number. 
    3. Ask the user to enter their total hours for the week. 
        Use their name as you did in step 2 when using input. 
        Save the answer into another variable. 
        The input of this step should be converted into an integer. 

    4. Calculate the total wages for the employee and save the result in a variable. 

    S. Show the result, using the output that resembles the following: 
        Sarah, your check for this week should be Sty where 
        Sarah should be replaced by the user's actual name and 
        tom is the total amount of the wages as a floating point number. 

It is important to: 
    use variables to get input, 
    think of the proper data type for each input, 
    and produce the proper output Use conversions when needed and
    do not add conversions if not needed as this causes point deductions. 

    Add comments to the top of the code stating your name and assignments. 
    Lack of such comments in this and every future assignment will cause point deductions. 

    If your code has any syntax errors, it will not execute, and this will cause 0 credit be given. 

    Submit your source code; you must upload your file - not copy and paste your code. No zipping please. 
"""

# Set variables
    # Employee name
name: str = ""
    # Hourly rate
rate: float = 0.00
    # Hours worked
hours: int = 0
    # Wages
wage: float = 0.00

# Get employee name
def getName():
    global name
    msg = "What is your name? "
    name = input(msg)

# Get hourly rate
def getRate():
    global name
    global rate
    msg = "what is hourly rate? "
    # Opting for f string to not change msg (by adding ", ...")
    rate = input(f"{name}, {msg}" )
    """ I could use 
        rate = float(input(f"{name}, {msg}" ) ) 
        But using functions in an input may be bad practice
        What's your take Prof. Jinan?
    """
    # 2:you should convert the into to a floating point number
    rate = float(rate)

# Hours worked in a week
def getHours():
    global name
    global hours
    msg = "what are the total hours you work for the week? "
    hours = input(f"{name}, {msg}" )
    # 3:The input of this step should be converted into an integer
    hours = int(hours)

# Calculate wages
def getwage():
    global name
    global rate
    global wage
    wage = rate * hours
    # 5: format wages as a floating point number
    wage = round(wage, 2)
    msg = f"{name}, your check for this week should be ${wage:,.2f}"
    print(msg)

# Let's roll!    
getName()
getRate()
getHours()
getwage()