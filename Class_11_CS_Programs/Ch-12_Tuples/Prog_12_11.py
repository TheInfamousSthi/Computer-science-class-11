# Program 12.11: Compare two tuples
# KEYWORD EXPLANATION:
# Lexicographical comparison operator checks tuples item by item starting from index 0.

tup1 = tuple(input("Enter elements for Tuple 1: ").split())
tup2 = tuple(input("Enter elements for Tuple 2: ").split())

if tup1 == tup2:
    print("Both tuples are equal")
elif tup1 > tup2:
    print("Tuple 1 is greater than Tuple 2")
else:
    print("Tuple 2 is greater than Tuple 1")
