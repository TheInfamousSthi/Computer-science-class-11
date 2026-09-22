# Program 12.8: Frequency of element in tuple
# KEYWORD EXPLANATION:
# tuple.count() - Counts occurrences of specified value within tuple.

tup = tuple(input("Enter space-separated elements: ").split())
key = input("Enter element to count: ")

print(f"Frequency of '{key}': {tup.count(key)}")
