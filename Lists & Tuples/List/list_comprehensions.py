# Problem 1 — Square Numbers
# Create a list of squares for numbers 1 to 10 using list comprehension.
new_list = [n**2 for n in range(1, 11)]
print(new_list)

print()
print()

# Problem 2 — Filter Even Numbers
# From a list of numbers, create a new list that only contains even numbers.
my_list = [1,2,4,3,2,5,3,5,3,6,7,8]
new_list = [n for n in my_list if n%2 == 0]
print(new_list)

print()
print()

# Problem 3 — Create a List of Strings with Condition
# From a list of words, create a list containing only those with length greater than 4.
my_list = ["a", "abc", "abcd","apple", "Banana", "Papaya"]
new_list = [s for s in my_list if len(s)> 4]
print(new_list)

print()
print()

# Problem 4 — Generate Multiplication Table (1 to 5)
# Use nested list comprehension to generate a list of (x, y, product) tuples.
new_list = [(n, k, n*k) for n in range(1,6) for k in range(1,11)]
print(new_list)

print()
print()

# Problem 5 — Conditional Expressions
# Replace all odd numbers in a list with the word “Odd”, keeping even numbers unchanged.
my_list = [1,2,3,4,5,6,7,8]
new_list = ["Odd" if n%2 != 0 else n for n in my_list ]
print(new_list)