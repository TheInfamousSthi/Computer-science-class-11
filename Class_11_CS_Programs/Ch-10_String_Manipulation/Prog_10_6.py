# Program 10.6: Character classification
# KEYWORD EXPLANATION:
# .isupper() - String method returning True if all characters are uppercase.
# .islower() - String method returning True if all characters are lowercase.
# .isdigit() - String method returning True if all characters are numerical digits.

text = input("Enter a string: ")

upper = lower = digits = special = 0

for char in text:
    if char.isupper():
        upper += 1
    elif char.islower():
        lower += 1
    elif char.isdigit():
        digits += 1
    else:
        special += 1

print("Uppercase characters:", upper)
print("Lowercase characters:", lower)
print("Digits:", digits)
print("Special characters:", special)
