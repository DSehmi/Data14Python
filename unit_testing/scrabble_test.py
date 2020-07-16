# Test Driven Development!

# Write unit tests first!

# Class!
# Scrabble score calculator
# Return the score for a word according to Scrabble letter points
# Randomly generate 7 tile hand
# Check that the word can be made using those tiles
# Once a word has been made, replace only used tiles

from scrabble import Scrabble
import unittest

my_scrabble_score = Scrabble


class ScrabbleTests(unittest.TestCase):

    def test_letter_points(self):
        self.assertEqual(Scrabble.letter_points("a"), 1)
        self.assertEqual(Scrabble.letter_points("d"), 2)
        self.assertEqual(Scrabble.letter_points("b"), 3)
        self.assertEqual(Scrabble.letter_points("f"), 4)
        self.assertEqual(Scrabble.letter_points("k"), 5)
        self.assertEqual(Scrabble.letter_points("j"), 8)
        self.assertEqual(Scrabble.letter_points("q"), 10)

    def test_find_score(self):
        self.assertEqual(Scrabble.find_score("python"), 14)
        self.assertEqual(Scrabble.find_score("encapsulation"), 17)
        self.assertEqual(Scrabble.find_score("abstraction"), 15)
        self.assertEqual(Scrabble.find_score("inheritance"), 16)
        self.assertEqual(Scrabble.find_score("polymorphism"), 26)

    def test_num_in_hand(self):
        self.assertEqual(Scrabble.num_in_hand(), 7)


