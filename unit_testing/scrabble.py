# Test Driven Development!

# Write unit tests first!

# Class!
# Scrabble score calculator
# Return the score for a word according to Scrabble letter points
# Randomly generate 7 tile hand
# Check that the word can be made using those tiles
# Once a word has been made, replace only used tiles
from random import randint


class ScrabbleScore:

    def find_score(self, word):
        points = {
            "a": 1, "b": 3, "c": 3, "d": 2, "e": 1, "f": 4, "g": 2, "h": 4, "i": 1,
            "j": 8, "k": 5, "l": 1, "m": 3, "n": 1, "o": 1, "p": 3, "q": 10, "r": 1,
            "s": 1, "t": 1, "u": 1, "v": 4, "w": 4, "x": 8, "y": 4, "z": 10
        }
        return sum([points[c] for c in word])
        # total = 0
        # for letter in word.lower():
        #     total += ScrabbleScore.points[letter]
        # return total

    def random_hand(self):
        hand = []
        for i in range(0, 7):
            random_letter = chr(randint(65, 90))
            hand.append(random_letter)

