# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 13:56:00 2024

@author: Omar Juvera

Write the definition of another function that 
takes two numbers, that represent speed in miles/hour and time in minutes. 
The function prints the distance traveled based on that speed and time. (1 points)
"""

speed: int = 0
minutes: int = 0
distance: float = 0.0

def distanceTraveled(varS, varM):
    varD: float = 0.0

    # Distance traveled
    varD = varS * (varM / 60)
    return varD

def main():
    s: int = 0
    m: int = 0
    d: float = 0.0

    # Get Speed
    s = input("What is the speed (mph)? ")
    s = int(s)

    # Get time (in minutes)
    m = input("In how many minutes? ")
    m = int(m)

    # Time machine
    d = distanceTraveled(s, m)
    print("The total distance traveled at", s, "mph in", m, "minutes is:", d, "miles")
    return s, m, d

speed, minutes, distance = main()
