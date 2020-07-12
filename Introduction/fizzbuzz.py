# FIZZBUZZ

# Start at 1
# Print each number in turn
# End at 100

# If divisible by 3, instead of number, "Fizz"
# If divisible by 5, instead of number, "Buzz"
# If divisible by both, instead of number, "FizzBuzz"

# EXTRA
# Accept user input for number to count up to? DONE
# Accept user input for number to start from? DONE
# Accept user input for custom fizz buzz? DONE
# Change the number we increment by. DONE
# Change values for fizz and buzz

# PEP8 = style guide for python. Read link sent.

# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz!")
#     elif number % 3 == 0:
#         print("Fizz!")
#     elif number % 5 == 0:
#         print("Buzz!")
#     else:
#         print(number)

# # custom user start and end values
# start = int(input("What number would you like to start from?\n"))
# end = int(input("What number would you like to end on?\n"))
#
# for number in range(start, end + 1):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz!")
#     elif number % 3 == 0:
#         print("Fizz!")
#     elif number % 5 == 0:
#         print("Buzz!")
#     else:
#         print(number)

# # custom user fizz and buzz words
# start = int(input("What number would you like to start from?\n"))
# end = int(input("What number would you like to end on?\n"))
# fizz = input("Fizz is pretty boring, what word would you prefer to use?\n")
# buzz = input("Buzz isn't actually that bad, but I know we can still do better...\n")
#
# for number in range(start, end + 1):
#     if number % 3 == 0 and number % 5 == 0:
#         print(fizz + buzz)
#     elif number % 3 == 0:
#         print(fizz)
#     elif number % 5 == 0:
#         print(buzz)
#     else:
#         print(number)

# # custom user increment value
# start = int(input("What number would you like to start from?\n"))
# end = int(input("What number would you like to end on?\n"))
# fizz = input("Fizz is pretty boring, what word would you prefer to use?\n")
# buzz = input("Buzz isn't actually that bad, but I know we can still do better...\n")
# increment = int(input("What increment value would you like to have?\n"))
#
# for number in range(start, end + 1, increment):
#     if number % 3 == 0 and number % 5 == 0:
#         print(fizz + buzz)
#     elif number % 3 == 0:
#         print(fizz)
#     elif number % 5 == 0:
#         print(buzz)
#     else:
#         print(number)
