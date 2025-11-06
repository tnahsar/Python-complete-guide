"""
Tuple unpacking in Python means assigning the elements of a tuple to multiple variables in a single statement.
- Tuple Unpacking: Extracting values directly into variables
    person = ("Alice", 30, "New York")
    # Tuple unpacking
    name, age, city = person
- Tuple Packing: Grouping multiple values together
- Swapping: Easily done using tuple unpacking
    a = 5
    b = 10
    a, b = b, a
"""
# Problem 1 — Tuple Unpacking
# Unpack a tuple (name, age, city) into three variables and print them.
my_tuple = ('prashant', 25, 'ahm')
name, age, city = my_tuple
print(f"Name: {name}, Age: {age}, City: {city}")

print()
print()

# Problem 2 — Swapping Without Temp Variable
# Swap values of two variables using tuple unpacking.
a = 5
b = 10
a, b = b, a

print(f"a: {a}, b: {b}")

print()
print()

# Problem 3 — Nested Tuple Access
# Given a tuple with nested data, access specific elements from it.
my_tuple = ((1,2), (3,4),(5,6))
element = my_tuple[2][0]
print(f"Element: {element}")

print()
print()

# Problem 4 — Returning Multiple Values
# Write a function that returns multiple values as a tuple.
def get_person_info():
    name = "prashant"
    age = 25
    city = "Ahm"
    return(name, age, city)
print(get_person_info())

print()
print()

# Problem 5 — Tuple of Tuples to List
# Convert a tuple of tuples into a single flattened list.
my_tuple = ((1,2), (3,4),(5,6))
my_list = [item for sub_tuple in my_tuple for item in sub_tuple]
print(my_list)