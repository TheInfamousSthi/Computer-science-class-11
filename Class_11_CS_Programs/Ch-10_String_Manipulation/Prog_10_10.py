# Program 10.10: Substring Replacement
# KEYWORD EXPLANATION:
# .replace(old, new) - Method replacing occurrences of 'old' substring with 'new' substring.

text = input("Enter main string: ")
old_sub = input("Enter substring to replace: ")
new_sub = input("Enter new substring: ")

modified_text = text.replace(old_sub, new_sub)

print("Original text:", text)
print("Modified text:", modified_text)
