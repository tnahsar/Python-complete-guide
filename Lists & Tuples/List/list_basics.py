# Problem 1:
# Create a list of 5 numbers and print the list.
list = [1,2,3,4,5]
print(list)

print()
print()

# Problem 2:
# Access the first and last element from the list and print them.
list = [1,2,3,4,5]
print(f"First element of {list} is: {list[0]}")
print(f"Last element of {list} is: {list[len(list)-1]}")

print()
print()

# Problem 3:
# Add a new element to the list using append() and print the updated list.
list = [1,2,3,4,5]
list.append(6)
print(list)

print()
print()

# Problem 4:
# Insert an element at a specific position using insert() and display the list.
list = [1,2,3,4,5]
list.insert(3,10)
print(list)

print()
print()

# Problem 5:
# Remove an element from the list using remove() and pop() methods.
list = [1,2,3,4,5]
list.remove(3) # Removes the first occurrence of a specific value.
list.pop(1) # Removes value at a specific position.
print(list)

print()
print()

# Problem 6:
# Ask user to input N numbers and form a list dynamically, then print it.
list_input = input("Enter N numbers and system will give you the list of all: ")
list = [int(d) for d in list_input]
print(list)

print()
print()