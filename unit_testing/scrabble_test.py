# Test Driven Development!

# Write unit tests first!

# Class!
# Scrabble score calculator
# Return the score for a word according to Scrabble letter points
# Randomly generate 7 tile hand
# Check that the word can be made using those tiles
# Once a word has been made, replace only used tiles

from scrabble import ScrabbleScore
import unittest

my_scrabble_score = ScrabbleScore()


class ScrabbleTests(unittest.TestCase):

    def test_find_score(self):
        self.assertEqual(my_scrabble_score.find_score("python"), 14)
        self.assertEqual(my_scrabble_score.find_score("encapsulation"), 17)
        self.assertEqual(my_scrabble_score.find_score("abstraction"), 15)
        self.assertEqual(my_scrabble_score.find_score("inheritance"), 16)
        self.assertEqual(my_scrabble_score.find_score("polymorphism"), 26)

