# file = open("order.txt")

# TYPE OF ERRORS

# ZeroDivision error
# Indentation error
# Name error
# ModuleNotFound error
# Syntax error
# Type error
# Key error
# Attribute error
# Index error
# Assertion error
# Recursion error

# try:
#     print("Trying to open the file...")
#     file = open("order.txt")
#     print("Successfully opened the file...")
# except FileNotFoundError as errmsg:  # try to include the specific exception that is estimated
#     print("Couldn't open the file! PANIC!")
#     print(errmsg)  # can alias the error and return the specific message
#     raise
# except FileExistsError:  # can use multiple except blocks
#     print("This will not happen but example of multiple except blocks")
# finally:  # (optional) this will run no matter what happens in the try/except blocks
#     print("Finished handling everything")
#
# print("This is the end of a file")
# # even if both errors are true,
# # python will only recognise the first error and then crash

# Different ways to read a file
# [r, w, x, a, t, b, +]
# r - Read Mode (default - if no file, fails)
# w - Write Mode (if no file, it creates one; if file, truncates)
# x - create mode (if file, fails)
# a - append mode (if no file, create one; if file, appends)
# t - text mode
# b - binary mode
# + - reading & writing


# def open_and_print_file(filename):
#     try:
#         opened_file = open(filename, "r")
#         file_line_list = opened_file.readlines()
#
#         for line in file_line_list:
#             print(line.rstrip('\n'))  # gets rid of spaces in between newlines
#
#         opened_file.close()
#
#     except FileNotFoundError:
#         print("File cannot be found, please check filename provided")
#         raise


# # open_and_print_file("order.txt")
#
# file = open("order.txt")
# order_lines = file.readlines()  # returns a list
# print(order_lines)
#
# print(file.readline())  # returns single first line
# print(file.readline())  # returns single second line
#
# # file.readline() doing this by itself will show the file but then remove it from the file

# with open("order.txt") as opened_file:  # same as line47
#     print(opened_file.readlines())


# def open_and_print_file(filename):
#     try:
#         with open(filename, "r") as opened_file:
#             file_line_list = opened_file.readlines()
#
#             for line in file_line_list:
#                 print(line.rstrip('\n'))  # gets rid of spaces in between newlines
#
#     except FileNotFoundError:
#         print("File cannot be found, please check filename provided")
#         raise
#
#
# open_and_print_file("order.txt")
# file = open("order.txt")
# order_lines = file.readlines()  # returns a list
# print(order_lines)
#
# with open("order.txt", "w") as changed_opened_file:
#     changed_opened_file.write("Cheeseburger\nPizza\nSpaghetti\nChow Mein")
#     file_line_list = changed_opened_file.readlines()


def append_to_file(filename, order):  # inputs are: the file, and what we want to append
    try:
        with open(filename, "a") as opened_file:
            # this with "w" would overwrite with only the last addition (kebab) remaining
            opened_file.write(order + '\n')
    except TypeError:
        print("Order needs to be a string. Please try again")


append_to_file("order.txt", "Pasta")
append_to_file("order.txt", "Hot Dog")
append_to_file("order.txt", "Kebab")
append_to_file("new_order.txt", "Pizza")
