# Program 9.13: Print Fibonacci series
# KEYWORD EXPLANATION:
# Simultaneous Assignment (a, b = b, a + b) - Evaluates right-side expressions before assignment.

n = int(input("Enter number of terms: "))

a, b = 0, 1
print("Fibonacci Series:")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()
