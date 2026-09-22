# Program 12.7: Search element in tuple
# KEYWORD EXPLANATION:
# tuple.index() - Returns position index of element inside immutable tuple.

tup = tuple(input("Enter tuple elements separated by space: ").split())
key = input("Enter element to search: ")

if key in tup:
    print(f"Element '{key}' found at index {tup.index(key)}")
else:
    print(f"Element '{key}' NOT found in tuple")
