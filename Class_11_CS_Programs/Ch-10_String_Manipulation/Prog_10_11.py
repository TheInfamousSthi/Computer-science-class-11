# Program 10.11: Count substring frequency
# KEYWORD EXPLANATION:
# .count(sub) - Method returning total non-overlapping occurrences of substring 'sub'.

text = input("Enter main string: ")
sub = input("Enter substring to search for: ")

count = text.count(sub)

print(f"The substring '{sub}' appears {count} times.")
