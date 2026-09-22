# Program 12.6: Swap Two Numbers using Tuple Assignment
# KEYWORD EXPLANATION:
# Tuple Assignment (a, b = b, a) allows variable value swapping without needing temporary variable.

a = input("Enter first value (a): ")
b = input("Enter second value (b): ")

print(f"Before swapping: a = {a}, b = {b}")

a, b = b, a

print(f"After swapping: a = {a}, b = {b}")
