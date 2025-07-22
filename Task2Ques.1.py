#Program to check wheather a number is even or odd

#Step1: Take an integer input from the user
number = int(input("Enter an integer:"))

#Step2: Check wheather the num is even or odd using if-else statement
if number % 2 == 0:
   print (f"{number}is Even")
else:
   print(f"{number}is odd")