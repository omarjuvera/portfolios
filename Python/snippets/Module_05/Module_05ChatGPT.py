# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 23:31:34 2024

@author: Omar Juvera
"""

"""
=========================================
================ ChatGPT ================
=========================================
"""


from random import randint
TotalPoints = 0  # Global variable for total points

def GenerateGuess(s, e):
    if s > 0 and s < e and (e - s) >= 10:
        return randint(1, e)
    return randint(1, 100)

def CheckGuess(user_guess, computer_guess):
    if user_guess == computer_guess:
        return 10
    elif abs(user_guess - computer_guess) <= 5:
        return 5
    else:
        return 0

def UpdatePoints(points):
    global TotalPoints
    TotalPoints += points

def main():
    global TotalPoints
    print("Let's play the number Guessing Game")      
    UserGuessRange = int(input("What range do you want to play for? "))
    ComputerGuess = GenerateGuess(1, UserGuessRange)
    
    UserGuess = int(input("Make a guess: "))
    
    Status = CheckGuess(UserGuess, ComputerGuess)
    
    if Status == 0:
        print("Sorry, you lost. The correct guess was:", ComputerGuess)
    else:
        UpdatePoints(Status)
        print("Congratulations! You earned", Status, "points. Total points:", TotalPoints)
    
    play_again = input("Do you want to play again? (yes/no): ").lower()
    
    if play_again == "yes":
        main()
    else:
        print("Goodbye! Total Points:", TotalPoints)

if __name__ == "__main__":
    main()
