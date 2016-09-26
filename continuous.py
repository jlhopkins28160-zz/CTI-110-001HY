#Johnny L. Hopkins
#September 21, 2016
#CTI 110-001HY: Web, Programming, and Database Foundations
#Dr. Dana Anderson
#continuous.py: Calculates interest compounded continuously
#Does not check input as it assumes users enters decimal values

import math

response = "Yes"

while response == "Yes" or response == "yes" or response == "y":
    principal = float(input("Enter your starting deposit (in decimal format): "))
    rate = float(input("What is the interest rate (in decimal format): "))
    time = float(input("Give the number of periods (in decimal format): "))
    balance = principal * math.exp(rate * time)
    print("Your new balance is {:.2f}".format(balance))

    response = input("Continue calculating interest?")
