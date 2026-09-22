# Program 11.7: List Element Frequency
# KEYWORD EXPLANATION:
# list.count(x) - Returns total number of times element x occurs in list.

lst = input("Enter list elements separated by space: ").split()
key = input("Enter element to count: ")

freq = lst.count(key)
print(f"Element '{key}' appears {freq} times in the list.")
