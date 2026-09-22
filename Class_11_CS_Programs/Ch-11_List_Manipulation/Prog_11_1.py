# Program 11.1: Dynamic List Creation
# KEYWORD EXPLANATION:
# [] - List notation defining mutable, ordered element sequences.
# .append() - List method adding an element to the end of the list.

n = int(input("Enter number of elements: "))
lst = []

for i in range(n):
    elem = input(f"Enter element {i+1}: ")
    lst.append(elem)

print("The created list is:", lst)
