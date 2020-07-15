# Map applies a function to an iterable
# Map is lazy! It returns a map object

# data14 = ["Katie", "Juxhen", "Joe"]
#
# print([x.upper() for x in data14])
# print(type([x.upper() for x in data14]))
#
# data14_upper = map(str.upper, data14)

# for name in data14_upper:
#     print(name)

# print(list(data14_upper))

# Write a function that squares a number and adds 3


def convert(x):
    return x**2 + 3


print(convert(4))

numbers = list(range(1, 10))


def square_add(num):
    return num * num + 3


num_map = map(square_add, numbers)
print(list(num_map))

