# Program 9.6: Display natural numbers from 1 to N
# KEYWORD EXPLANATION:
# for - Loop keyword used for sequence iteration.
# range(start, stop) - Built-in function generating arithmetic progression of integers.
# end - Keyword argument in print() controlling character appended at end.

n = int(input("Enter N: "))

print(f"Natural numbers from 1 to {n}:")
for i in range(1, n + 1):
    print(i, end=" ")
print()
