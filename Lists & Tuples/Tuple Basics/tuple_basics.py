# Problem 13:
# Create a tuple containing 5 items and print it.
my_tuple = (1,2,3,4,5)
print(tuple)

print()
print()

# Problem 14:
# Access 2nd and 4th element of the tuple.
my_tuple = (1,2,3,4,5)
print(f"Second element from tuple is: {tuple[2]}")
print(f"fourth element from tuple is: {tuple[4]}")

print()
print()

# Problem 15:
# Try to modify an element and observe what happens (immutability demo).
my_tuple = (1,2,3,4,5)
#tuple[2] = 10 #Uncomment to see the error
#print(f"Second element from tuple is: {tuple[2]}")


# Problem 16:
# Convert the tuple into a list, add an element, and convert it back to a tuple.
my_tuple = (1,2,3,4,5)
list = [int(d) for d in my_tuple]
#list.append(7)
# convert the list back to a tuple (avoid reassigning built-in names)
new_tuple = tuple(list)
print(new_tuple)

print()
print()

# Problem 17:
# Perform slicing on the tuple (e.g., first 3 elements, last 2 elements).
my_tuple = (1,2,3,4,5)
print(f"First three elements of tuple are: {tuple[0:3]}")       # slicing in python is start-inclusive and stop-exclusive
print(f"Last two elements of tuple are: {tuple[3:5]}")          # slicing in python is start-inclusive and stop-exclusive

print()
print()

# Problem 18:
# Ask user for 3 numbers and store them as a tuple. Then unpack the tuple into 3 separate variables and print them individually.
first_number = input("Enter first number: ")
second_number = input("Enter second number: ")
third_number = input("Enter third number: ")
new_tuple = (first_number, second_number, third_number)
print(new_tuple)
a = new_tuple[0]
b = new_tuple[1]
c = new_tuple[2]
print(f"a = {a} + b = {b} + c = {c}")