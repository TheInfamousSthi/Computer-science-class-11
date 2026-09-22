# Program 10.3: Palindrome Check
# KEYWORD EXPLANATION:
# String Slicing [start:stop:step] - text[::-1] reverses a string using step -1.

text = input("Enter a string: ")

if text == text[::-1]:
    print("The string is a Palindrome")
else:
    print("The string is NOT a Palindrome")
