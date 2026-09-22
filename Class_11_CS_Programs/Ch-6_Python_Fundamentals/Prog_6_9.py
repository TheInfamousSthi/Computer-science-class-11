# Program 6.9: Simple Interest and Compound Interest
# KEYWORD EXPLANATION:
# type() - Returns the data type of an object/variable.
# id() - Returns unique memory address identifier assigned to a variable.

P = float(input("Enter Principal amount: "))
R = float(input("Enter Rate of Interest: "))
T = float(input("Enter Time period (years): "))

# Display data type and memory identity
print("Data type of Principal:", type(P))
print("Memory address ID of Principal:", id(P))

# Simple & Compound interest calculation
SI = (P * R * T) / 100
CI = P * ((1 + R / 100) ** T) - P

print("Simple Interest =", SI)
print("Compound Interest =", CI)
