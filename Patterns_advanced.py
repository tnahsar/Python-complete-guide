# Problem : Butterfly Pattern (Star Version) — Most Asked in Interviews
# *      *
# **    **
# ***  ***
# ********
# ********
# ***  ***
# **    **
# *      *
k = 6
for i in range(1,5):
    print("*" * i + " " * k + "*" * i)
    k -= 2
j = 0
for i in range(4, 0, -1):
    print("*" * i + " " * j + "*" * i)
    j += 2

print(" ")
print(" ")

# Problem: Hourglass Pattern (Solid and Hollow Versions)
# *********
#  *******
#   *****
#    ***
#     *
#    ***
#   *****
#  *******
# *********
a = 0
for i in range(9, 1, -2):
    print(" " * a + "*" * i + " " * a)
    a += 1
b = 4
print(" " * b + "*")

b -= 1
for i in range(3, 10, +2):
    print(" " * b + "*" * i)
    b -= 1

print(" ")
print(" ")

# Problem: Floyd’s Triangle (It is a right-angled triangular array of natural numbers)
# 1
# 2 3
# 4 5 6
# 7 8 9 10
k = 1
for i in range(1, 5):
    for j in range(1, i+1):
        print(k, end = " ") # end=" ", it tells Python to replace the usual newline (\n) with a space (" "), which means the next printed value will be on the same line separated by a space instead of being on a new line.
        k += 1
    print()

print(" ")
print(" ")

# Problem: Pascal’s Triangle (Logic-based, not formula-heavy)
#      1
#    1   1
#  1   2   1
# 1  3   3   1
triangle = []
    # Loop to generate each row
for i in range(10):
        # Start each row with a list of ones
    row = [1] * (i + 1)
        
        # Fill in the middle elements of the row
    for j in range(1, i):
        row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        
        # Add the row to the triangle
    triangle.append(row)
    
    # Print the triangle
for row in triangle:
    print(" ".join(map(str, row)).center(10 * 2))  # Center-align each row

print(" ")
print(" ")

triangle = []

for i in range(5):
    row = [1] * (i+1)
    print(row)

    for j in range(1, i):
        row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        print(row)
    
    triangle.append(row)
    print(triangle)