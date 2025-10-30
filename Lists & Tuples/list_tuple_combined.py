# Problem 19:
# Find the largest and smallest number in a list without using max() or min() (use loops).
my_list = [1,5,10,8,3,2]
max = 0
for d in my_list:
    a = d
    if a > max:
        max = a
    else:
        max = max
print(f"maximum number from the list is: {max}")

min = 1
for d in my_list:
    a = d
    if a < min:
        min = a
    else:
        min = min
print(f"minimum number from the list is: {min}")

print()
print()


# Problem 20:
# Remove duplicate elements from a list.
my_list = [1,2,5,6,2,1,3,4,5]
new_list = list(set(my_list))
print(new_list)



# Problem 21:
# Given two lists, find the common elements.
my_list1 = [1,2,3,4,5]
my_list2 = [3,4,5,6,7]
common_elements = []
for d in my_list1:
    if d in my_list2:
        print(d)
        common_elements.append(d)
    else:
        print()
print(f"Common elements are: {common_elements}")
        
print()
print()

# Problem 22:
# Count the frequency of each element in a list and display the result (hint: dictionary or nested loop).
my_list = [1,3,4,3,2,4,5,6,23,1,3,9]

frequency = {}
for d in my_list:
    frequency[d] = frequency.get(d,0) + 1
print(frequency)
#print("Element frequencies:")
#for key, value in frequency.items():
#    print(f"{key}:{value}")

print()
print()

# Problem 23:
# Convert a list of tuples into a dictionary.
# Example: [("name", "Prashant"), ("age", 25)] → {"name": "Prashant", "age": 25}
my_list = [(1,2), ('a','b')]
my_dict = {}
for t in my_list:
    my_dict[t[0]] = t[1]
print(my_dict)

print()
print()

# Problem 24: Accept a list of integers from the user. Remove all duplicates.
# Sort the unique numbers in ascending order. Print the 2nd largest unique number.
user_input = input("Enter a list of integers, separated by spaces: ")
my_list = list(map(int,user_input.split()))
print(f"list of user input integers is: {my_list}")
unique_list = list(set(my_list))
print(f"Unique list is: {unique_list}")
unique_list.sort()
print(f"Sorted (asc) unquie list is: {unique_list}")
len_unique_list = len(unique_list)
print(len_unique_list)
print(f"2nd largest unique number from the list is: {unique_list[len_unique_list-2]}")
