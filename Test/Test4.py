# Ask the user to enter a number
# Calculate the sum of its digits
# Example: 123 → 1 + 2 + 3 = 6
# Hint: Convert number to string OR use % and // math)
num = int(input("Enter the number(N) and system will tell sum of digits of the number: "))
digits = [int(d) for d in str(num)]
total = sum(d for d in digits)
print(total)


# Ask the user to enter a full sentence
# Count how many words are in it
# Input: "Learning Python is fun" → Output: 4
# Hint: split() method breaks sentence into a list of words
sentence = str(input("Enter the sentence and system will tell you how many words it have in it: "))
words = sentence.split()
total_words = len(words)
print(total_words)


# Check if a Number is a Perfect Number
# A Perfect Number is a number that is equal to the sum of its proper divisors (excluding itself)
# Example:
# 6 → divisors: 1, 2, 3 → 1+2+3 = 6 ✅
# 28 → divisors: 1, 2, 4, 7, 14 → 1+2+4+7+14 = 28 ✅
# Ask the user for a number and check if it’s perfect.
num = int(input("Enter a number(N) and system will tell you whether its a perfect number or not: "))
total = sum(i for i in range(1, num) if num % i == 0)
if total == num:
	print(f"{num} is a perfect number")
else:
	print(f"{num} is not a perfect number")
	

# Ask the user to enter a number
# Print the largest digit from it
# Example: 58341 → Largest digit = 8
num = int(input("Enter a number(N) and system will tell you the largest digit among all the digits in the number: "))
digits = [int(i) for i in str(num)]
print(digits)
largest_digit = max(digits)
print(largest_digit)


# Ask the user to enter a number
# Count how many digits are even and how many are odd
# Example: 12345 → Even = 2 (2,4), Odd = 3 (1,3,5)
num = int(input("Enter a number and system will tell you count of even and odds digits in a number: "))
digits = [int(d) for d in str(num)]
even_count = [d for d in digits if d % 2 == 0]
odd_count = [d for d in digits if d % 2 != 0]
total_even_digits = len(even_count)
total_odd_digits = len(odd_count)
print(f"Total even digits in a {num} are {total_even_digits}")
print(f"Total odd digits in a {num} are {total_odd_digits}")