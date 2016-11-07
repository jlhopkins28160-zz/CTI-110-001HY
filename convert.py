#Programmer: Johnny L. Hopkins
#Date: October 11, 2016
#Course: CTI 110-001HY: Web, Programming, and Database Fundamentals
#Instructor: Dr. Dana Anderson
#convert.py: Converts a temperature taking Fahrenheit as input and outputs the Celsius temperature to the screen
#Uses the format function to round all converted temperatures to two significant digits

response = "Yes"
while response == "Yes" or response == "yes" or response == "YES" or response == "Y" or response == "y":
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = 5.0/9.0 * (fahrenheit - 32.0)
    n = format(celsius, '.2f')
    print("The equivalent in Celsius is", n)
    response = input("Do you want to continue?")
