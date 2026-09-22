# Program 9.7: Sum of natural numbers from 1 to N
# KEYWORD EXPLANATION:
# += - Augmented assignment operator combining addition and assignment (sum = sum + i).

n = int(input("Enter N: "))
total_sum = 0

for i in range(1, n + 1):
    total_sum += i

print(f"Sum of natural numbers from 1 to {n} is: {total_sum}")
