# Program 12.1: Tuple Traversal
# KEYWORD EXPLANATION:
# tuple() - Constructor converting iterable objects into immutable tuples.

tup = tuple(input("Enter space-separated tuple elements: ").split())

print("Traversing tuple:")
for item in tup:
    print(item)
