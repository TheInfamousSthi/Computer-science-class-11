# Program 6.3: Calculate area of a rectangle
# KEYWORD EXPLANATION:
# eval() - Evaluates Python expressions passed as strings (e.g., dynamically converts "5.5" to float or "5" to int).
# * - Arithmetic multiplication operator.

length = eval(input("Enter length of rectangle: "))
breadth = eval(input("Enter breadth of rectangle: "))

# Calculate area
area = length * breadth

print("Length =", length)
print("Breadth =", breadth)
print("Area of rectangle =", area)
