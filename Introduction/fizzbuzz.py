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


# # 1. Initial fizzbuzz

# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)


# # 2. Custom user start and end values

# start = int(input("What number would you like to start from?\n"))
# end = int(input("What number would you like to end on?\n"))
#
# for number in range(start, end+1):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)


# # 3. Custom user fizz and buzz words

# start = int(input("What number would you like to start from?\n"))
# end = int(input("What number would you like to end on?\n"))
# fizz = input("Fizz is pretty boring, what word would you prefer to use?\n")
# buzz = input("Buzz isn't that bad, but I know we can still choose a better word...\n")
#
# for number in range(start, end+1):
#     if number % 3 == 0 and number % 5 == 0:
#         print(fizz+buzz)
#     elif number % 3 == 0:
#         print(fizz)
#     elif number % 5 == 0:
#         print(buzz)
#     else:
#         print(number)


# # 4. Custom user increment value

# start = int(input("What number would you like to start from?\n"))
# end = int(input("What number would you like to end on?\n"))
# fizz = input("Fizz is pretty boring, what word would you prefer to use?\n")
# buzz = input("Buzz isn't actually that bad, but I know we can still do better...\n")
# increment = int(input("What increment value would you like to have?\n"))
#
# for number in range(start, end+1, increment):
#     if number % 3 == 0 and number % 5 == 0:
#         print(fizz+buzz)
#     elif number % 3 == 0:
#         print(fizz)
#     elif number % 5 == 0:
#         print(buzz)
#     else:
#         print(number)


# # 5. Custom values for fizz and buzz

# start = ""
# end = ""
# fizz_value = ""
# buzz_value = ""
# increment = ""
#
# while not start.isnumeric():
#     start = input("What number would you like to start from?\n")
#     if not start.isnumeric():
#         print("That is not a number, try again")
#
# start = int(start)
#
# while not end.isnumeric():
#     end = input("What number would you like to end on?\n")
#     if not end.isnumeric():
#         print("That is not a number, try again")
#
# end = int(end)
#
# while not fizz_value.isnumeric():
#     fizz_value = input("What fizz number would you like?\n")
#     if not fizz_value.isnumeric():
#         print("That is not a number, try again")
#
# fizz_value = int(fizz_value)
#
# while not buzz_value.isnumeric():
#     buzz_value = input("What buzz number would you like?\n")
#     if not buzz_value.isnumeric():
#         print("That is not a number, try again")
#
# buzz_value = int(buzz_value)
#
# while not increment.isnumeric():
#     increment = input("What increment value would you like to have?\n")
#     if not increment.isnumeric():
#         print("That is not a number, try again")
#
# increment = int(increment)
#
# fizz_word = input("Fizz is a pretty rubbish word, what else can we use?\n")
# buzz_word = input("Buzz isn't actually that bad, but I know we can still do better...\n")
#
# for number in range(start, end+1, increment):
#     if number % fizz_value == 0 and number % buzz_value == 0:
#         print(fizz_word+buzz_word)
#     elif number % fizz_value == 0:
#         print(fizz_word)
#     elif number % buzz_value == 0:
#         print(buzz_word)
#     else:
#         print(number)


# 6. Add Functions


def number_check(prompt):
    number = input(prompt)
    if number.isnumeric():
        number = int(number)
    else:
        print("Please enter a number in number format")
    return number


start = number_check("Please enter a start number\n")
end = number_check("Please enter an end number\n")
increment_level = number_check("Please enter an increment level\n")
fizz_value = int(input("What Fizz number would you like?\n"))
buzz_value = int(input("What Buzz number would you like?\n"))
fizz_word = input("Fizz is a pretty rubbish word, what else can we use?\n")
buzz_word = input("Buzz isn't actually that bad, but I know we can still do better...\n")


def fizzbuzz(start_number, end_number, increment):
    for number in range(start_number, end_number+1, increment):
        if number % fizz_value == 0 and number % buzz_value == 0:
            print(fizz_word+buzz_word)
        elif number % fizz_value == 0:
            print(fizz_word)
        elif number % buzz_value == 0:
            print(buzz_word)
        else:
            print(number)


print(fizzbuzz(start, end, increment_level))



