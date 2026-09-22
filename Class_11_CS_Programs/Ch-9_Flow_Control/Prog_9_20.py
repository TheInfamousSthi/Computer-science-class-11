# Program 9.20: Check Armstrong Number
# KEYWORD EXPLANATION:
# while - Loop executing repeatedly as long as conditional statement evaluates to True.
# str() - Type conversion function converting numbers/data into text strings.
# len() - Built-in function returning character/item count of sequences.

num = int(input("Enter a number: "))
temp = num
num_digits = len(str(num))
sum_pow = 0

while temp > 0:
    digit = temp % 10
    sum_pow += digit ** num_digits
    temp //= 10

if sum_pow == num:
    print(num, "is an Armstrong Number")
else:
    print(num, "is NOT an Armstrong Number")
