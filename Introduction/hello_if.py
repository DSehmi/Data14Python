# CONTROL FLOW

# IF statements, FOR statements, WHILE loops


# if <conditional statement>:
#   <result>
# <result whether or not in conditional statement>

# indentation is important


# age = 15
# if age > 18:
#     print("You can see the scary film")
#
# print("Watch frozen or something")
#

# # elif & else
#
# if age > 18:
#     print("You can see the scary film")
# elif age == 18:
#     print("You are only just old enough")
# else:
#     print("You are too young, go away")

# # EXERCISE
#
# film_rating = "18"
#
# if film_rating == "U":
#     print("Suitable for all ages")
# elif film_rating.upper() == "PG":
#     print("Suitable with parental guidance")
# elif film_rating.upper() == "12A" or film_rating == "12":
#     print("Suitable for ages 12 and over")
# elif film_rating == "15":
#     print("Suitable for ages 15 and over")
# elif film_rating == "18":
#     print("Suitable for ages 18 and over")
# else:
#     print("Please enter a valid film rating")
#
# # ALTERNATE SOLUTION
#
# ratings = {
#     "U": "Suitable for all ages",
#     "PG": "Parental Guidance required",
#     "12A": "Suitable for ages 12 and over",
#     "15": "Suitable for ages 15 and over",
#     "18": "Suitable for ages 18 and over"
# }

# age = 6
# adult_present = True
#
# if age > 12:
#     print("Come on in")
# else:
#     if adult_present:
#         print("Come on in")
#     else:
#         print("Get an adult")

