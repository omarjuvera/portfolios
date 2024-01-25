# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 13:09:12 2024

@author: Omar Juvera

Write the definition of a function that 
takes one number, that represents a temperature in Fahrenheit. 
The function prints the equivalent temperature in degrees Celsius. (1 point)

conversion formula: f = c * (9/5)  + 32 
"""

f: float = 0.00
c: float = 0.00

def convertToFarenheits(varC):
    varF : float = 0.00

    # Convert C to F. Formula: f = c * (9/5)  + 32 
    varF = varC * (9/5)  + 32

    # Return result
    return varF


def main():
    tempF: float = 0.00
    tempC: float = 0.00

    # Get celcius temperture from user
    tempC = input("What is the temperture, in celcius?: ")
    tempC = float(tempC)

    # Convert to farenheits
    tempF = convertToFarenheits(tempC)
    print("The temperture, in Fahrenheit is", tempF)
    
    # Return temperture values to user
    return tempF, tempC
    

f, c = main()