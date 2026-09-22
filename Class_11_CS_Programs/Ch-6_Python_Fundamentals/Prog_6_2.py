# Program 6.2: Obtain three numbers and print their sum
# KEYWORD EXPLANATION:
# input() - Reads string input from the keyboard.
# float() - Type conversion function converting string/int into a floating-point number.
# print() - Outputs specified data to the console terminal.

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Calculate sum of inputs
sum_val = num1 + num2 + num3

# Output results
print("The numbers entered are:", num1, num2, num3)
print("Sum of the three numbers is:", sum_val)
