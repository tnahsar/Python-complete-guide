# Problem 7:
# Find the maximum and minimum values from a list.
list = [1,4,3,5,3,2,7]
print(f"Maximum number from the list is: {max(list)}")
print(f"Manimum number from the list is: {min(list)}")

print()
print()

# Problem 8:
# Sort the list in ascending and descending order.
list = [3,5,6,9,1,3,6,2,1]
list.sort()
print(f"Ascending order of list is: {list}")
list.sort(reverse=True)
print(f"Desending order of list is: {list}")

print()
print()

# Problem 9:
# Reverse the list and display it.
list = [ 3,4,5,7,21,5,9,1,0,3]
list.reverse()
print(f"Reverse of list is: {list}")

print()
print()

# Problem 10:
# Count how many times a particular element appears in the list.
list = [3,4,5,7,21,5,9,1,0,3,5,6,3]
count = list.count(3)
print(f"Occurence of 3 is {count} times")

print()
print()

# Problem 11:
# Demonstrate list slicing by printing sub-parts of the list (first 3 elements, last 2 elements, etc.)
list = [1,2,4,5,6,9,2,3,5,2,8]
print(f"{list[3:9]}")  # slicing in python is start-inclusive and stop-exclusive

print()
print()

# Problem 12:
# Accept a sentence from the user and convert it into a list of words using split().
sentence = input("Enter a sentence and system will give a list of words: ")
sentence.split()
#words = [str(w.split(" ")) for w in sentence]
print(f"List of words in a given sentence is: {sentence.split()}")