# Program 12.12: Mean of Tuple elements
# KEYWORD EXPLANATION:
# Statistical mean computation combining sum() and len().

numbers = tuple(float(x) for x in input("Enter space-separated numbers: ").split())

if numbers:
    mean = sum(numbers) / len(numbers)
    print("Mean of tuple elements:", mean)
else:
    print("Tuple is empty")
