# Program 11.15: Separate Odd and Even Numbers
# KEYWORD EXPLANATION:
# List Comprehension [expr for item in iterable if condition] - Concise syntax for building lists.

numbers = [int(x) for x in input("Enter space-separated integers: ").split()]

evens = [x for x in numbers if x % 2 == 0]
odds = [x for x in numbers if x % 2 != 0]

print("Original list:", numbers)
print("Even numbers:", evens)
print("Odd numbers:", odds)
