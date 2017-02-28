#Johnny L. Hopkins
#February 26, 2017
#compounding.py: A new program based on algorithm to calculate Continuous interest

import math

response = "Yes"
while response == "Yes" or response == "YES" or response == "yes" or response == "y" or response == "Y":
    principal = float(input("Enter your starting balance: "))
    rate = int(input("Enter your interest rate as a percent: "))
    time = int(input("Enter the time of compounding as an integer: "))

    #Takes rate as interger and convert to decimal
    converted_rate = rate / 100

    new_balance = principal * math.exp(converted_rate * time)

    #Format to two decimal places
    print("Your new balance is $", '{0:.2f}'.format(new_balance))

    response = input("Do you want to continue?")

    

print("Thank you for using the Continuous Compounding program. Good Bye!")