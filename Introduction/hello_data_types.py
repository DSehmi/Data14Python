# # Numbers
# # String
# # Boolean
#
# # NUMBERS
#
# # Add
# print(1 + 1)
#
# # Subtract
# print(1 - 1)
#
# # Multiply
# print(2 * 2)
#
# # Divide (will always return a decimal, not an integer)
# print(12 / 3)
#
# # Modulo (Remainder)
# print(14 % 3)
#
# # Greater Than
# a = 10
# b = 5
# print(a > b)
#
# # Less Than
# print(b < a)
#
# # Greater than or equal to
# c = 10
# print(c >= a)
#
# # Less than or equal to
# print(a <= c)
#
# # Is equal to
# print(a == c)
#
# # Is not equal to
# print(b != c)
#
# # Numeric Types: int, float, complex
# a = 1
# b = 2.5
# c = 3 + 2j
#
# print(a, b, c)
# print(type(a), type(b), type(c))
# print(a + c)
#
# # STRINGS
#
# single = 'Single Quotes'
# double = "Double Quotes"
#
# # Using quote inside a string
# single_inside = "I'm using single quotes"
# print(single_inside)
#
# slash = "I\'m using single quotes"
# print(slash)
#
# # Using both quotes in a string
# both = "So I'm saying \"Help\""
# print(both)
#
# # Select certain characters from a string
# # NOTE python starts counting at 0
#
# hw = "Hello World!"
# print(hw)
# print(hw[4])
#
# # 0 1 2 3 4 5 6 7 8 9 10 11
# # H e l l o   W o r l d  !
#
# print(hw[3:7])
# # This prints from 3 up to BUT NOT INCLUDING 7
#
# print(hw[3:])
# # This prints from 3 to the end of the string
#
# print(hw[:8])
# # This prints from the beginning up to but not including 8th
#
# print(hw[-2])
# # This prints the second character FROM THE END
#
# print(hw[-5:])
# # This prints from the 5th last character to the end
#
# print(len(hw))
# # This prints the length of the string which is 12, NOTE there is no 12th character because counting starts at 0
#
# # STRING METHODS AND FUNCTIONS
#
# white_space = "    bunch of white space       "
#
# print(len(white_space))
# print(white_space)
#
# # These methods strip the string of its complete, left or right white space
# print(white_space.strip())
# print(white_space.lstrip())
# print(white_space.rstrip())
# # Methods are applied to a specific thing with a .
#
# # Count the amount of substrings in your string
# print(white_space.count(" "))
#
# # Change case of string
# print(white_space.lower())
# print(white_space.upper())
#
# # Replace Substrings
# print(white_space.replace("white", "blank"))
#
# # Method Stringing - using multiple methods in one go
#
# # Capitalise only works when there is not white space at beg so we use both functions together
# print(white_space.strip().capitalize())
#
# # Concatenate
# a = "Alien"
# b = "Bat"
# c = "Car"
# print(a + ", " + b + ", " + c)
#
# # Can only concatenate strings together
# d = 5
# # print(a + " " + b + " " + c + " " + d) - this will not work
# print(a + ", " + b + ", " + c + ", " + str(d))
#
# # F String converts all elements into strings
# print(f"{a}, {b}, {c}, {d}")
#
# name = "Danvir"
# print(f"Hello, my name is {name}!")
#
# # Exercise
# name = input("What is your name?\n")
# age = int(input("How old are you?\n"))
# num_siblings = int(input("How many siblings do you have?\n"))
# fav_decimal = float(input("What is your favourite decimal?\n"))
# fav_animal = input("What is your favourite animal?\n")
# # Turning a data type into another data type is called CASTING
#
# print(f"So your name is {name}, you are {age} years old,
# you have {num_siblings} siblings, your favourite decimal is {fav_decimal} for some reason,
# and finally your favourite animal is a {fav_animal}.")
#
# print(type(name))
# print(type(age))
# print(type(num_siblings))
# print(type(fav_decimal))
# print(type(fav_animal))

# # BOOLEANS
#
# a = True
# b = False
# # capitalisation is required
# age = 19
# weather = "sunny"
#
# print(a == b)
# print(a != b)
# print(a > b)
# print(True and True)
# print(True and False)
# print(True or False)
# print(age > 18 and weather == "sunny")

# hw = "Hello World!"
# print(hw.isalpha()) # alphabetic characters only
#
# print(hw.islower()) # checks if all letters are lower case
# hw = "hello world!"
# print(hw.islower())
#
# hw = "HELLO WORLD!"
# print(hw.isupper()) # checks if all letters are upper case
#
# hw = "Hello World!"
# print(hw.startswith("x")) # checks if string begins with specified character
# print(hw.startswith("H"))
#
# print(hw.endswith("x")) # checks if string ends with specified character
# print(hw.endswith("!"))

x = 0
y = 6
z = -4
a = "hello"
b = ""
print(bool(x))
print(bool(y))
print(bool(z))
print(bool(a))
print(bool(b))
# boolean of 0 is false, boolean of any other number (positive or negative) is true
# boolean of any string is true, unless there are no characters

n = None
print(bool(n))
# None is similar to NULL in SQL, often used as a placeholder
