# Program 9.14: Check Prime Number
# KEYWORD EXPLANATION:
# break - Control flow statement exiting loop immediately upon execution.
# True, False - Boolean literal keywords representing logical values.

num = int(input("Enter a number: "))

if num > 1:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, "is a Prime Number")
    else:
        print(num, "is NOT a Prime Number")
else:
    print(num, "is NOT a Prime Number")
