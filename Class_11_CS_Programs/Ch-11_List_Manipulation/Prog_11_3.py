# Program 11.3: Max and Min in List
# KEYWORD EXPLANATION:
# .split() - String method splitting text into list elements based on delimiter space.
# min() - Built-in function returning smallest item in iterable.

numbers = [int(x) for x in input("Enter space-separated integers: ").split()]

if numbers:
    print("List:", numbers)
    print("Maximum element:", max(numbers))
    print("Minimum element:", min(numbers))
else:
    print("List is empty")
