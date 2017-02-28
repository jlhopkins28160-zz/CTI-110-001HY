#Johnny L. Hopkins
#February 26, 2017
#compound.py: Calculates compound interest
import math

response = "Yes"
while response == "Yes" or response == "YES" or response == "yes" or response == "Y" or response == "y":
    principal = float(input("Enter your starting deposit: "))
    annual_rate = int(input("Enter the annual interest rate: "))

    #Convert annual interest rate to decimal value
    new_annual_rate = annual_rate / 100

    #Number of times we compund principal
    period = int(input("Enter the number of compounding periods: "))
     
    #Period of time(years) we compound principal
    time = int(input("Enter the number of years for your investment: "))

    future_value = principal * math.pow((1 + (new_annual_rate / period)), (period * time))
    print("The future value of your original investment is $", '{0: .2f}'.format(future_value))

    response = input("Do you want to continue?")

print("Exiting program! Good-Bye!")
