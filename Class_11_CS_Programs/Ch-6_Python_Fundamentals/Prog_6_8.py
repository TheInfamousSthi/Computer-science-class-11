# Program 6.8: Compute triangle area using Heron's Formula
# KEYWORD EXPLANATION:
# import - Module import keyword used to include external built-in packages.
# math.sqrt() - Standard math library function returning square root of a number.

import math

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

# Semi-perimeter calculation
s = (a + b + c) / 2

# Heron's formula implementation
area = math.sqrt(s * (s - a) * (s - b) * (s - c))

print("Semi-perimeter (s) =", s)
print("Area of triangle =", area)
