  #Displays the results of each operation on the screen.
 # Taking input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Performing basic mathematical operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# Handling division by zero
if num2 != 0:
    division = num1 / num2
else:
    division = "Undefined (cannot divide by zero)"

# Displaying the results
print("\nResults of Mathematical Operations:")
print("Addition:       ", addition)
print("Subtraction:    ", subtraction)
print("Multiplication: ", multiplication)
print("Division:       ", division)
