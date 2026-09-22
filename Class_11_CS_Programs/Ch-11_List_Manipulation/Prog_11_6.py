# Program 11.6: Linear Search
# KEYWORD EXPLANATION:
# .index(item) - List method returning lowest zero-based index where item is found.

lst = input("Enter list elements separated by space: ").split()
key = input("Enter element to search: ")

if key in lst:
    print(f"Element '{key}' found at index {lst.index(key)}")
else:
    print(f"Element '{key}' NOT found in list")
