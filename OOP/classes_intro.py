# Classes are the blueprints for objects
# Classes can have attributes and methods (a method is function but inside a class)
# Don't use underscores for spaces, just use snake casing


# class GoodDog:
#     animal_type = "Canine"  # Attribute (variable)
#
#     def bark(self):  # Method (function)
#         return "Woof!"
#
#
# fluffy = GoodDog()  # Created an instance of the class (an Object)
# print(fluffy.animal_type)
# print(fluffy.bark())

# class Dog:
#
#     def __init__(self):  # Initialisation (runs instantly)
#         self.name = "Jimmy"
#         self.legs = 4
#         self.animal_type = "Canine"
#
#     def bark(self):
#         return "Woof!"
#
#
# big_dog = Dog()
# small_dog = Dog()
#
# print(big_dog.name)
# print(small_dog.legs)
# print(big_dog.animal_type)
#
# print("-------HORRIBLE CURSE-------")
#
# Dog.animal_type = "Arachnid"
# Dog.legs = 8
#
# print(big_dog.animal_type)
# print(small_dog.legs)
#
# medium_dog = Dog()
# medium_dog.animal_type = "Canine"
# medium_dog.legs = 4
#
# print(medium_dog.animal_type)
# print(medium_dog.legs)


class Dog:

    def __init__(self, name, colour ):  # Initialisation
        self.name = name
        self.colour = colour
        self.legs = 4
        self.animal_type = "Canine"
        self._secret = "I can't eat chocolate"  # Underscore after dot - private variable

    def bark(self):
        return "Woof!"

    def introduce(self):
        return f"Hello there, my name is {self.name} and I am a {self.colour} {self.animal_type}"

    def get_secret(self):  # known as GETTER
        return self._secret

    def set_secret(self, secret):  # SETTER
        self._secret = secret


new_dog = Dog("Pablo", "golden")  # Instantiation
print(new_dog.introduce())

print(new_dog.get_secret())
print(new_dog.set_secret("I hid my bone in the garden"))
print(new_dog.get_secret())



