# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 20:21:34 2024

@author: Omar Juvera
"""

from random import randint
totalPoints = 0


def GenerateGuess(s,e):
    if (s < e) and (s > 0): #According to my research 0 is not a positive number. Hence s>0
        # This logic below is broken. Why go to the trouble to ask a user for their deried RANGE to just upend the decission?
        # If the user wants a range of 1 to 7, return should be randint(1, 7) not (1,100)
        # The condition "at least 10" should not exsist. In my opinion
        if abs(s - e) >= 10:
            return (randint(1, e))
    return randint(1, 100)


def CheckGuess(user, pc):
    if user == pc:
        return 10
    elif abs(user - pc) <= 5:
        return 5
    else:
        return 0

def UpdatePoints(points):
    global totalPoints
    #totalPoints = totalPoints + points
    totalPoints += points


def main():
    print("Let's play the number Guessing Game")
    userGuessRange = input("What range do you want to play for (e.g., 1-11? ")

    # Since the specs had some flaws....GenerateGuess(?????, userGuessRange)
    # I will split userGuessRange input into two variables AND apply int()
    userGuessMin, userGuessMax = map(int, userGuessRange.split('-'))
    computerGuess = GenerateGuess(userGuessMin, userGuessMax)

    userGuess = int(input("Guess a number: "))
    status = CheckGuess(userGuess , computerGuess)

    if status == 0: 
    # Display a loosing message
        print("Sorry, you lost. The correct guess was:", computerGuess)
        print("Your total points are:", totalPoints)
    else:
    # Display a winning message
        print("Congratulations! You've earned", status)
        UpdatePoints(status)
        print("Your total points are:", totalPoints)

    # Ask if the user wants to play again. If user types 'yes', call main. 
    again = input("Do you want to play again? (yes/no): ")
    again = again.lower()

    # Play again?
    if again == "yes":
        main()
    else:
        print("Goodbye! Total Points:", totalPoints)

main()
