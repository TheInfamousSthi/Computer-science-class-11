# Program 12.2: Find Length of Tuple without len()
# KEYWORD EXPLANATION:
# _ (Underscore) - Used as throwaway variable indicator when loop variable isn't referenced inside loop body.

tup = tuple(input("Enter space-separated elements: ").split())
count = 0

for _ in tup:
    count += 1

print("Tuple:", tup)
print("Length of tuple (without len()):", count)
