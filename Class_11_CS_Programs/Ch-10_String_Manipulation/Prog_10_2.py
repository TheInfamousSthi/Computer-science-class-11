# Program 10.2: Count vowels in string
# KEYWORD EXPLANATION:
# Sequential membership test using 'in' operator on string literals.

text = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0

for char in text:
    if char in vowels:
        count += 1

print("Total vowels in string:", count)
