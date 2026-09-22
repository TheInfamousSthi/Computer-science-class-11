# Program 6.4: Convert height in cm to feet and inches
# KEYWORD EXPLANATION:
# int() - Converts float/string to integer by truncating decimal values.
# // - Floor division operator (returns integer quotient without remainder).
# % - Modulus operator (returns remainder of division).
# f"" - Formatted string literal allowing direct insertion of expressions inside {}.

height_cm = float(input("Enter height in cm: "))

total_inches = height_cm / 2.54
feet = int(total_inches // 12)
inches = total_inches % 12

print(f"Height: {feet} feet and {inches:.2f} inches")
