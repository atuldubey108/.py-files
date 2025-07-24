import math

#Step1: Ask the user for a number

number = float(input("Enter a number:"))


#Step2: Calculate Square root, natural log, and sine

square_root = math.sqrt(number)
natural_log = math.log(number)
sine_value = math.sin(number) #assume input is in radians

#Step3: Display the result

print("\nResult:")
print("Square Root of", number, "is:", square_root)
print("Natural Log (ln) of", number, "is:", natural_log)
print("Sine of", number, "(in radians) is:", sine_value)