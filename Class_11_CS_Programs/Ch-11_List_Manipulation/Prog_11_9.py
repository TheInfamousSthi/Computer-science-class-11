# Program 11.9: Remove Duplicates
# KEYWORD EXPLANATION:
# not in - Negative membership test operator.

lst = input("Enter list elements separated by space: ").split()
unique_lst = []

for item in lst:
    if item not in unique_lst:
        unique_lst.append(item)

print("Original list:", lst)
print("List after removing duplicates:", unique_lst)
