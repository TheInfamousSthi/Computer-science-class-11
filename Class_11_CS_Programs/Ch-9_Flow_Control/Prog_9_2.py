# Program 9.2: Find largest of two numbers
# KEYWORD EXPLANATION:
# elif - Short for "else if", used for multi-branch conditional checks.
# max() - Returns largest item from given arguments.

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if num1 > num2:
    print(num1, "is larger")
elif num2 > num1:
    print(num2, "is larger")
else:
    print("Both numbers are equal (using max():", max(num1, num2), ")")
