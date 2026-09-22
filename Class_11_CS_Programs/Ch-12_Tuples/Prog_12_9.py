# Program 12.9: Tuple Slicing
# KEYWORD EXPLANATION:
# Tuple Slicing [start:stop:step] extracts sliced tuple segments.

tup = (10, 20, 30, 40, 50, 60, 70, 80)

print("Original tuple:", tup)
print("First 4 elements:", tup[:4])
print("Elements from index 2 to 5:", tup[2:6])
print("Every second element:", tup[::2])
print("Reversed tuple:", tup[::-1])
