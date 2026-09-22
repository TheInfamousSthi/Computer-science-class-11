# Program 11.5: Sum and Average of List
# KEYWORD EXPLANATION:
# sum() - Built-in function summing numeric items within iterable sequence.

numbers = [float(x) for x in input("Enter space-separated numbers: ").split()]

if numbers:
    total = sum(numbers)
    avg = total / len(numbers)
    print("Sum =", total)
    print("Average =", avg)
else:
    print("No numbers provided")
