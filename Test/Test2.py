
# Multiplication Table
# Ask the user to enter a number.
# Print its multiplication table up to 10.
# Example (for 5):
num = int(input("Enter the number for which you need the table: "))
for x in range(1, 11): #range function is inclusive of the start value and exclusive of the end value.
    print(f"{num} x {x} = {num * x}")


# Count vowels in a word
# Ask the user to enter a word.
# Count how many vowels (a, e, i, o, u) it has.
# Print the count.
# Hint: loop through characters and check if in "aeiou"
string = str(input("Enter any string and we will tell you how many vowels it has: "))
vowels = "aeiouAEIOU"
count = 0
for char in string:
    if char in vowels:
        count += 1
print(f"String is having {count} vowels in it")


# Sum of first N natural numbers
# Ask the user to enter a number N.
# Print the sum of numbers from 1 to N.
# Example: if N = 5, output = 15 (because 1+2+3+4+5).
# Hint: use a loop OR the formula n*(n+1)//2
num = int(input("Enter a number (N) to get the sum of all natural numbers from 1 to N: "))
total = 0
for i in range(1, num + 1):
    total += i
print(total)



# Factorial of a number
# Ask the user to enter a number.
# Print its factorial.
num = int(input("Enter a number (N) to get the factorial of the number: "))
factorial = 1
for i in range(num, 0, -1):
    factorial *= i
print(factorial)


# Reverse a string (without using slicing)
# Ask the user to enter a word.
# Print it in reverse using a loop.
# Hint: start from last character and build the new string
string = str(input("Enter the string to get the reverse of it: "))
reverse_string = ""
for char in string:
  reverse_string = char + reverse_string
print(reverse_string)


# Count digits and letters in a string
# Ask the user to enter any string (e.g., "Python123").
# Count how many characters are digits and how many are letters.
# Print the result.
# Hint: use .isalpha() and .isdigit()
s = (input("Enter a string to get the count of digits and letters in string: "))
total_digits = 0
total_letter = 0
total_specialCharacter_or_whitespace = 0
for char in s:
    if char.isdigit():
        total_digits += 1
    elif char.isalpha():
        total_letter += 1
    else:
        total_specialCharacter_or_whitespace +=1
print(f"Total digits in string are: {total_digits} and total letters are: {total_letter} and total special_characters_or_whitespace = {total_specialCharacter_or_whitespace}")
    
    
    