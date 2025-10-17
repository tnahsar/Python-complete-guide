# Output:
# *
# **
# ***
# ****
# *****
for i in range(1, 6):
    print("*" * i)


print(" ")
print(" ")

# Output:
# *****
# ****
# ***
# **
# *
for i in range(5, 0, -1):
    print("*" * i)


print(" ")
print(" ")

# Output:
# 1
# 12
# 123
# 1234
# 12345
for i in range(1, 6):
    output = []
    for i in range (1, i+1):
        output.append(i)
    print(*output)  # * is called the unpacking operator or splat operator. It takes an iterable (such as a list, tuple, or set) and "unpacks" it, passing each individual element as a separate argument to the function.


print(" ")
print(" ")

# Output:
#     *
#    **
#   ***
#  ****
# *****
j = 5
for i in range(1, 6):
    print(" " * j + "*" * i)
    j -= 1