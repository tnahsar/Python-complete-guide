# Output:
#     *
#    ***
#   *****
#  *******
# *********
j = 4
for i in range(1, 10, +2):
    print(" " * j + "*" * i + " " * j) 
    j -= 1

print()
print()

# Output:
# *********
#  *******
#   *****
#    ***
#     *
j = 0
for i in range(9, 0, -2):
    print(" " * j + "*" * i + " " * j) 
    j += 1

print()
print()

# Output:
# *****
# *   *
# *   *
# *   *
# *****
for i in range(6, 1, -1):
    if i == 6 or i == 2:
        print("*" * 5)
    else:
        print("*" + " " * 3 + "*")

print()
print()

# Output:
# *
# **
# * *
# *  *
# *****
for i in range(1, 6):
    if i == 3 or i == 4:
        print("*" + " " * (i-2) + "*")
    else:
        print("*" * i)

print()
print()

# Output:
#     *
#    * *
#   *   *
#  *     *
# *********
k = 4
for i in range(1,10,2):
   if i == 1:
       print(" " * k + "*" + " " * k)
       k -= 1
   elif i == 9:
       print("*" * i)
   else:
       print(" " * k + "*" * (i-(i-1)) + " " * (i-2) + "*" * (i-(i-1)) + " " * k)
       k -= 1