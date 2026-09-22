# Program 11.8: Reverse a List
# KEYWORD EXPLANATION:
# .reverse() - List method modifying list in-place (or slicing [::-1] returning reversed copy).

lst = input("Enter list elements separated by space: ").split()
print("Original list:", lst)

reversed_lst = lst[::-1]
print("Reversed list:", reversed_lst)
