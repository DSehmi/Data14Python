# Don't
# Repeat
# Yourself

# Syntax - def <function_name>():


# def print_multiple_times(string, number_of_times):
#     string_to_print = string * number_of_times
#     print(string_to_print)
#
#
# print_multiple_times("Woo hoo! ", 3)


# def repeat_string(string_to_repeat, number_of_repeats):
#     string_to_return = string_to_repeat * number_of_repeats
#     return string_to_return
#
#
# eg_string = repeat_string("Example ", 5)
# print(eg_string)

# # Addition Function
# def addition(first_number, second_number):
#     return first_number + second_number
#
#
# eg_addition = addition(4, 46)
# print(eg_addition)


# # Set Default Value
# # Better to set the default value for the end parameter, not for the first parameter
#
# def repeat_string(string_to_repeat, number_of_repeats=3):
#     string_to_return = string_to_repeat * number_of_repeats
#     return string_to_return
#
#
# print(repeat_string("Woo hoo! "))

# # Multiple Arguments, use * to denote this
#
# def find_product(*multiargs):
#     for num in multiargs:
#         print(num)
#
#
# find_product(1, 2, 3, 4, 5)


# # Create function that multiplies all arguments together
# def find_product(*multiargs):
#     if len(multiargs) < 1:
#         return None
#     else:
#         product = 1
#         for number in multiargs:
#             product = product * number
#         return product
#
#
# print(find_product(1, 4, 6))


# Data Type Hints (Does not enforce, just hint)
def repeat_string(string_to_repeat: str, number_of_repeats: int = 3) -> str:
    string_to_return = string_to_repeat * number_of_repeats
    return string_to_return


print(repeat_string("Woo hoo! ", 3).upper())
