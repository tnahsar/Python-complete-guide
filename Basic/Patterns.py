# Problem — Print Solid Diamond Pattern
# Output:
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *
j = 4
k = 0
for i in range(1,10,2):
    print(" " * j + "*" * i + " " * j)
    j -= 1
for i in range(7, 0, -2):
    print(" " * k, "*" * i, " " * k)
    k += 1


print(" ")
print(" ")

# Problem — print X Pattern with Stars
# Output:
# *   *
#  * *
#   *
#  * *
# *   *
j = 3
for i in range(0,2):
    print(" " * i + "*" + " " * j + "*")
    j -= 2
print(" " * 2 + "*" + " " * 2)
k = 1
for i in range(1,4,+2):
    print(" " * k + "*" + " " * i + "*")
    k -= 1

print(" ")
print(" ")

# Problem - Print Hollow Diamond
#     *
#    * *
#   *   *
#  *     *
# *       *
#  *     *
#   *   *
#    * *
#     *
print(" " * 4 + "*")
a = 3
b = 1
for i in range(1,4):
    print(" " * a + "*" + " " * b + "*")
    a -= 1
    b += 2
c = 0
d = 7
for i in range(1,5):
    print(" " * c + "*" + " " * d + "*")
    c += 1
    d -= 2 
print(" " * 4 + "*")