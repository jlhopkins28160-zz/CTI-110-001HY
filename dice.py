#Johnny L. Hopkins
#September 25, 2016
#CTI 110-001HY: Web, Programming, and Database Foundations
#Dr. Dana Anderson
#dice.py: A program simualting the rolling of two dice. 

from random import randint

roll = "Yes"

while roll == "Yes" or roll == "yes" or roll == "y":
    x = randint(1,6)
    y = randint(1,6)

    diceroll = x + y
    print("You rolled a " +str(diceroll))
    roll = input("Do you want to roll again?")


