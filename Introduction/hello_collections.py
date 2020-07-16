# # collections are the way we can combine multiple things together
#
# # LISTS aka Arrays, denoted by square brackets []
# shopping_list = ["eggs", "sausages", "cheese", "bread"]
# print(shopping_list)
# print(type(shopping_list)) # type returns 'list'
#
# # we can combine data types within a list
# # we can even contain lists within a list
# shopping_list = ["eggs", "sausages", "cheese", "bread", 5, 2.5, True, [1, 2, 3]]
# print(shopping_list)
#
# # can specify a single value/range of values just like we do with strings
# print(shopping_list[0])
# print(shopping_list[-5])
# print(len(shopping_list))
#
# # add something to a list using a list method
# shopping_list.append("mushrooms")
# print(shopping_list)
#
# shopping_list.append("coffee")
# print(shopping_list)
#
# # remove something from list
# shopping_list.remove("cheese")
# print(shopping_list)
#
# # remove last item from list. Printing the pop function returns the item that was removed
#
# print(shopping_list.pop())
# print(shopping_list)

# #TUPLES - denoted by normal brackets ()
#
# colours = ("blue", "purple", "turquoise")
# print(colours)
# print(type(colours))
# print(colours[-1])
#
# # tuples are immutable (cannot be changed) i.e. <tuple>.remove() will not work
#
# print(colours.count("blue"))
# print(colours.index("blue"))

# DICTIONARIES

# denoted by curly brackets {}
# uses key value pairs. key must be unique and value can be anything

# my_dict = {"key": "value", "key2": 2}
# print(type(my_dict))
# print(my_dict)
#
# bigger_dictionary = {
#     "key1": "value1",
#     "key2": 2,
#     "key3": [1, 2, 3, 4]
# }
# print(bigger_dictionary)
#
# # Exercise
# danny_dictionary = {
#     "name": "Danvir",
#     "age": 23,
#     "dob": "24/01/1997",
#     "num_siblings": 3,
#     "fav_animal": "wolf"
# }
# print(danny_dictionary)
#
# # Access dictionaries by using square brackets - <dict>[key]
# print(danny_dictionary["name"])
#
# #  Reassign values
# my_dict["key"] = "new_value"
#
# # Insert new keys
# my_dict["new_key"] = "new key value"
#
# # Delete key
# del my_dict["new_key"]
#
# # dictionaries do not have an order
# # we can look up values using a key, but you cannot find a key based on the value as values do not have to be unique
#
# print(my_dict.keys())
# print(my_dict.values())

# #EXERCISE

# data14_dict = {
#     "Course": "Data_Engineering",
#     "Subjects": ["Business Skills", "SQL", "Data Concepts", "Agile", "Python"],
#     "Schedule": {
#         "Week 1": "Business Skills",
#         "Week 2": "SQL",
#         "Week 3": "Data Concepts",
#         "Week 4": ["Agile", "Python"]
#     },
#     "Trainer": "David_Harvey",
#     "Location": "Remote",
#     "Participants": 11,
#     "Start_Date": "15/06/20",
#     "Enjoying?": True
# }
#
# print(data14_dict)
#
# data14_dict["Company"] = "Sparta Global"
# print(data14_dict)
# del data14_dict["Start_Date"]
# print(data14_dict)
# # Access elements of a list within a dictionary
# print(data14_dict["Subjects"][0])
# print(data14_dict["Schedule"]["Week 4"])

# # SETS are unordered lists - denoted by curly brackets but without keys:values
#
# car_parts = {"wheels,", "doors", "steering wheel"}
# print(car_parts)
#
# # cannot print(car_parts(0)) as there is no order to sets
#
# # Add elements
# car_parts.add("pedals")
# print(car_parts)
#
# # Remove elements
# car_parts.discard("doors")
# print(car_parts)
#
# # FROZEN SET - an immutable set
# fs = frozenset([1, 2, 3, 4])
# print(fs)


