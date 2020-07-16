# Encapsulation
# Abstraction
# Inheritance
# Polymorphism
# cd onedrive/week5/4_pillars_of_OOP

class Animal:
    def __init__(self, name, legs):
        self.name = name
        self.legs = legs
        self._hunger = 5
        print("I exist.")

    def breathe(self):
        print("Breathing in...")
        print("Breathing out...")
        self._hunger += 0.1

    def eat(self):
        print("Nom nom nom")
        self._hunger = 0


class Mammal(Animal):
    def __init__(self, name, colour):
        super().__init__(name, 4)
        self.colour = colour

    def give_birth(self):
        print("I have given live birth")


class Dog(Mammal):
    def __init__(self, name, colour):
        super().__init__(name, colour)

    def wag_tail(self):
        print("Swish swish")
        super().breathe()
        self._hunger += 1


class Chihuahua(Dog):
    def feisty(self):
        print("I am angry all the time. I may be small but don't mess with me!!!")


class Bat(Mammal):
    def __init__(self, name, colour):
        super().__init__(name, colour)
        self.legs = 2


class Platypus(Mammal):
    def __init__(self, name, colour):
        super().__init__(name, colour)

    def give_birth(self):
        print("I have laid an egg")


my_bat = Bat("Bruce", "Black")
print(my_bat.give_birth())
my_platypus = Platypus("Perry", "Blue")
print(my_platypus.give_birth())

# Avoid having long inheritance chains

