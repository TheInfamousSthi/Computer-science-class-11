# Program 12.3: Max, Min, Sum of Tuple
# KEYWORD EXPLANATION:
# Numeric Tuple processing using built-in min(), max(), and sum().

tup = tuple(float(x) for x in input("Enter space-separated numbers: ").split())

if tup:
    print("Tuple:", tup)
    print("Maximum:", max(tup))
    print("Minimum:", min(tup))
    print("Sum:", sum(tup))
else:
    print("Empty tuple")
