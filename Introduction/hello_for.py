# # FOR LOOPS
#
# shopping_list = ["eggs", "bacon", "bread"]
# favourite_colours = ["yellow", "purple", "turquoise"]
#
# for item in shopping_list:
#     print(item)
#
# for item in shopping_list:
#     for colour in favourite_colours:
#         print(item, colour)
# # we are looping through a list within a list - this returns all possible combinations of items and colours

# dict_data = {
#     1: {"Name": "Alex", "Animal": "Dog"},
#     2: {"Name": "Ben", "Animal": "Flamingo"},
#     3: {"Name": "Evie", "Animal": "Gorilla"},
#     4: {"Name": "Charlotte", "Animal": "Giraffe"}
# }
#
# # Print keys
# for key in dict_data:
#     print(key)
#
# # Print values
# for key in dict_data:
#     print(dict_data[key])
#
# # Print Values of the Inner Dictionary
# for key in dict_data:
#     for inner_key in dict_data[key]:
#         print(dict_data[key][inner_key])
#
# for key in dict_data:
#     print(f"{dict_data[key]['Name']}'s favourite animal is {dict_data[key]['Animal']}")

# #EXERCISE
#
# chinese_menu = {
#     101: {'dish': 'egg fried rice', 'price': 1.60},
#     102: {'dish': 'prawn chow mein', 'price': 2.50},
#     103: {'dish': 'sweet chilli chicken', 'price': 4.50},
#     104: {'dish': 'satay sauce', 'price': 1.50},
#     105: {'dish': 'lamb in black bean sauce', 'price': 4.50}
# }
#
# for key in chinese_menu:
#    print(chinese_menu[key])
# for key in chinese_menu:
#     print(f"The dish {chinese_menu[key]['dish']} will cost {chinese_menu[key]['price']:.2f}.")

# print(list(range(10)))
#
# for number in range(10):
#     print(number)