
# Scrabble Game
# Classes:
# Tile - keeps track of the tile letter and value
# Rack - keeps track of the tiles in a player's letter rack
# Bag - keeps track of the remaining tiles in the bag
# Word - checks the validity of a word and its placement

# Keeps track of the score-worth of each letter-tile.
values = {"A": 1, "B": 3, "C": 3, "D": 2, "E": 1, "F": 4, "G": 2, "H": 4,
          "I": 1, "J": 1, "K": 5, "L": 1, "M": 3, "N": 1, "O": 1, "P": 3,
          "Q": 10, "R": 1, "S": 1, "T": 1, "U": 1, "V": 4, "W": 4, "X": 8,
          "Y": 4, "Z": 10}


class Tile:
    def __init__(self, letter, letter_values):
        self.letter = letter.upper()
        if self.letter in letter_values:
            self.score = letter_values[self.letter]
        else:
            self.score = 0

    def get_letter(self):
        return self.letter

    def get_score(self):
        return self.score


class Bag:
    # creates the bag of all letters available in the game
    def __init__(self):
        self.bag = []
        self.initialise_bag()

    def add_to_bag(self, letter, quantity):
        for i in range(quantity):
            self.bag.append(letter)

    def initialise_bag(self):
        global values
        self.add_to_bag(Tile("A", values), 9)
        self.add_to_bag(Tile("B", values), 2)
        self.add_to_bag(Tile("C", values), 2)
        self.add_to_bag(Tile("D", values), 4)
        self.add_to_bag(Tile("E", values), 2)
        self.add_to_bag(Tile("F", values), 2)
        self.add_to_bag(Tile("G", values), 3)
        self.add_to_bag(Tile("H", values), 2)
        self.add_to_bag(Tile("I", values), 9)
        self.add_to_bag(Tile("J", values), 9)
        self.add_to_bag(Tile("K", values), 1)
        self.add_to_bag(Tile("L", values), 4)
        self.add_to_bag(Tile("M", values), 2)
        self.add_to_bag(Tile("N", values), 6)
        self.add_to_bag(Tile("O", values), 8)
        self.add_to_bag(Tile("P", values), 2)
        self.add_to_bag(Tile("Q", values), 1)
        self.add_to_bag(Tile("R", values), 6)
        self.add_to_bag(Tile("S", values), 4)
        self.add_to_bag(Tile("T", values), 6)
        self.add_to_bag(Tile("U", values), 4)
        self.add_to_bag(Tile("V", values), 2)
        self.add_to_bag(Tile("W", values), 2)
        self.add_to_bag(Tile("X", values), 1)
        self.add_to_bag(Tile("Y", values), 2)
        self.add_to_bag(Tile("Z", values), 1)

    def take_from_bag(self):
        return self.bag.pop()

    def get_remaining_tiles(self):
        return len(self.bag)


class Hand:
    def __init__(self, bag):
        self.hand = []
        self.bag = bag
        self.initialise()

    def add_to_hand(self):
        self.hand.append(self.bag.take_from_bag())

    def initialise(self):
        for i in range(7):
            self.add_to_hand()

    def get_hand_str(self):
        return ", ".join(str(item.get_letter()) for item in self.hand)

    def get_hand_arr(self):
        return self.hand

    def remove_from_hand(self, tile):
        self.hand.remove(tile)

    def get_hand_length(self):
        return len(self.hand)

    def replenish_hand(self):
        while self.get_hand_length() < 7 and self.bag.get_remaining_tiles() > 0:
            self.add_to_hand()


class Player:

    def __init__(self, bag):
        self.name = ""
        self.hand = Hand(bag)
        self.score = 0

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def get_hand_str(self):
        return self.hand.get_hand_str()

    def get_hand_arr(self):
        return self.hand.get_hand_arr()

    def increase_score(self, increase):
        self.score += increase

    def get_score(self):
        return self.score

    def calculate_word_score(self):
        global values
        word_score = 0
        for letter in self.word:
            word_score += values[letter]
        self.player.increase_score(word_score)
