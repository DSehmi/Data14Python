# FILTER
# Anything that returns true for first part of filter bracket gets printed
# Using the second part of the bracket as the source

students = ["DAVID", "Lee", "RICHARD"]
result = filter(str.isupper, students)
print(list(result))

# Write function that returns True if a number is even and divisible by 3


def number(x):
    return x % 6 == 0


print(number(7))

numbers = list(range(1, 100))
print(list(filter(number, )))  # pm check recording 47:00

words = ["CAT", "BIRD", "BREAD", "BASKET"]


def check_easy(word):
    return len(word) == 3 or len(word) == 4


print(list(filter(check_easy, words)))
