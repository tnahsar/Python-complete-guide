"""
Slicing in Python is a way to extract a portion (or a subsequence) of a sequence like a list, string, or 
tuple by specifying a start index, stop index, and an optional step.

General syntax for slicing is:sequence[start:stop:step]
- start: The index where the slice begins (inclusive). If omitted, it defaults to the beginning of the sequence (0).
- stop: The index where the slice ends (exclusive). If omitted, it defaults to the end of the sequence.
- step: How many steps to move forward between elements. Defaults to 1.

IMP: Slicing in python is start-inclusive and stop-exclusive
"""

# Problem 1: Ask the user for a string and extract the characters from index 1 to 4
my_string = str(input("Enter a string for slicing examples: "));
print(f"get characters from index 1 to 4: {my_string[1:4]}")

print()
print()

# Problem 2: Ask the user for a string and extract the characters from the start to a specific index
my_string = str(input("Enter a string for slicing examples: "));
print(f"Slice from the start to a specific index: {my_string[:4]}")

print()
print()

# Problem 3: Ask the user for a string and extract the characters from specific index to the end
my_string = str(input("Enter a string for slicing examples: "));
print(f"Slice from a specific index to the end: {my_string[3:]}")

print()
print()

# Problem 4: Ask the user for a string and extract the characters while skipping certain by using step
my_string = str(input("Enter a string for slicing examples: "));
print(f"Skip characters using step: {my_string[::2]}")
# Example consider string = Python then output would be Pto
# From start to end, take every 2nd character (`'P'`, `'t'`, `'o'`)

print()
print()

# Problem 5: Ask the user for a string and reverse a substring
print(f"Reverse a substring: {my_string[1:5][::-1]}")