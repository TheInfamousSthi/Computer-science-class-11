# Program 12.13: Nested Tuples
# KEYWORD EXPLANATION:
# Index chaining [i][j] accesses elements inside nested structures.

nested_tup = (("Roll No", 1), ("Name", "Rhea"), ("Subject", "CS"))

print("Nested tuple structure:")
for item in nested_tup:
    print(f"Key: {item[0]} -> Value: {item[1]}")
