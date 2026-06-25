# Prime Number Checker
# Ask the user to enter a number.
# Check if it’s prime (only divisible by 1 and itself)
# Print whether it’s prime or not
# Hint: A number is prime if no number from 2 to n-1 divides it evenly
num = int(input("Enter a number and system will tell you whether its prime number or not: "))
output = ""
if num < 2:
    print("Number is not prime") # 0 and 1 are not prime
else:
    isprime = False
    for i in range(2, num):
        if num % i != 0:
            isprime = True
        else:
            isprime = False

    if isprime == True:
        output = "Number is prime"
    else:
        output ="Number is not prime"
    print(output)


# Fibonacci Sequence Generator
# Ask the user to enter a number N.
# Print the first N numbers in the Fibonacci sequence
# Example: For N=6, output → 0, 1, 1, 2, 3, 5
# Hint: start with 0 and 1, then keep adding previous two numbers
num = int(input("Enter the number (N) and system will give the fibonacci series till N: "))
a = 0
b = 1
c = 1
for i in range(num):
    print(a)
    a = b
    b = c
    c = a + b


# Armstrong Number Checker
# An Armstrong number is a number that is equal to the sum of its digits raised to the power of the number of digits.
# Example:
# 153 = 1³ + 5³ + 3³ = 153 ✅
# 9474 = 9⁴ + 4⁴ + 7⁴ + 4⁴ = 9474 ✅
# Ask the user for a number, check if it’s Armstrong or not.
num = int(input("Enter the number(N) and system will tell whether its Armstrong or not: "))
def isArmstrong(num):
    digits = [int(d) for d in str(num)] #list comprehension in Python, which is a compact way to generate a list.
    power = len(digits)
    total = sum(d ** power for d in digits)
    return total == num

if isArmstrong(num):
    print(f"{num} is Armstrong number")
else:
    print(f"{num} is not a Armstrong number")


# Check if a Number is a Strong Number
# A Strong Number is a number where the sum of factorial of its digits equals the number itself.
# Example:
# 145 → 1! + 4! + 5! = 1 + 24 + 120 = 145 ✅
# 40585 → 4! + 0! + 5! + 8! + 5! = 40585 ✅
num = int(input("Enter the number(N) and system will tell whether its Strong or not: "))
digits = [int(d) for d in str(num)]

def factorial(d):
    fact = 1
    for i in range(d, 1, -1):
        fact *= i
    return fact

output = []
for d in digits:
    a = factorial(d)
    output.append(a)
#print(output)    
total = sum(d for d in output)
#print(total)
if total == num:
    print(f"{num} is a strong number")
else:
    print(f"{num} is not a strong number")
