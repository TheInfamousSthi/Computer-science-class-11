# Program 11.10: Sort List
# KEYWORD EXPLANATION:
# sorted() - Built-in function returning new sorted list from items in iterable.
# reverse=True - Keyword argument specifying descending sort order.

numbers = [int(x) for x in input("Enter space-separated numbers: ").split()]

asc_sorted = sorted(numbers)
desc_sorted = sorted(numbers, reverse=True)

print("Original list:", numbers)
print("Ascending order:", asc_sorted)
print("Descending order:", desc_sorted)
