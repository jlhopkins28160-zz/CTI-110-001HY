#Johnny L. Hopkins
#October 19, 2016
#CTI 110-001HY: Web, Database, and Programming Foundations
#Dr. Dana Anderson
#conditions.py: Illustrate the use of if...else statements using temperature conversions to guide output.

#Welcome user
print("Welcome to the conversion program.")
print("I can take your Celsius temperature as input")
print("I can then tell you what you should wear")
print("Let's get started, shall we?")

#Convert temperature
celsius = float(input("Enter temperature in celsius:"))
fahrenheit = ((9/5) * celsius) + 32

#Give fashion advise based on temperature
if fahrenheit > 70:
    print("Your temperature is: ", fahrenheit)
    print("Wear shorts, it's hot out there today!")
elif fahrenheit < 70:
    print("Your temperature is: ", fahrenheit)
    print("Wear long pants, it's a blizzard outside!")
else:
    print("ERROR!, Out of range")

input("Press <Enter> to continue.")
