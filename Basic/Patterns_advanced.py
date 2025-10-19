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