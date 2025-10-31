# Problem: Print your name and age
# Ask the user to enter their name and age using input()
# Print them back in a sentence: "Hello <name>, you are <age> years old."
name = input("Enter you name: ");
age = int(input("Enter your age: "));
print(f"Hello {name}, you are {age} years old.");


# Problem: Simple calculator (addition)
# Ask the user to enter two numbers
# Add them and print the result
num1 = int(input("Enter first number: "));
num2 = int(input("Enter second number: "));
print(f"The sum of {num1} and {num2} is {num1 + num2}");


# Problem: Find the square of a number
# Ask the user to enter a number
# Print its square
print(f"The square of {num1} is {num1*num1}");
print(f"The square of {num2} is {num2**2}"); #**2 means power of number raised to power of 2


# Problem: Raise a number to the power of 10
# Ask the user to enter a number
# Print its value
print(f"The {num1} power of 10 is {num1**10}");


# Prblem: Even or Odd checker
# Ask the user to enter a number
# Print whether it’s even or odd
if num1%2 == 0:
    print(f"{num1} is even")
else:
    print(f"{num1} is odd")

# Problem: Find the largest of two numbers
# Ask the user to enter two numbers
# Print which one is larger (or if they’re equal)
# (Hint: use if-elif-else)
if num1 > num2:
    print(f"{num1} is greater than {num2}");
elif num1 < num2:
    print(f"{num1} is smaller than {num2}");
else:
    print(f"{num1} is equal to {num2}");

# Problem 2: Check if a word is a palindrome
# A palindrome is a word that reads the same backward and forward.
# Examples: madam, level, racecar.
# Ask the user to enter a word.
# Print whether it is a palindrome.
# (Hint: reverse a string with slicing → word[::-1])
string = str(input("Enter a word, system will tell you whether its palindrome or not: "));
string = string.lower(); # To make it case-insensitive (Madam → palindrome), you can add:
reverse_string = string[::-1]; #using -1 reverses the string by moving backward.
if string == reverse_string:
    print("Word is palindrome")
else:
    print("Word is not palindrome")
