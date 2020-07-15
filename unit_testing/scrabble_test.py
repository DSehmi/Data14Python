# Test Driven Development!

# Write unit tests first!

# Class!
# Scrabble score calculator
# Return the score for a word according to Scrabble letter points
# Randomly generate 7 tile hand
# Check that the word can be made using those tiles
# Once a word has been made, replace only used tiles

from scrabble import ScrabbleScore

my_scrabble_score = ScrabbleScore()


def test_letter_points():
    assert my_scrabble_score.letter_points("u") == 1
    assert my_scrabble_score.letter_points("d") == 2
    assert my_scrabble_score.letter_points("m") == 3
    assert my_scrabble_score.letter_points("f") == 4
    assert my_scrabble_score.letter_points("k") == 5
    assert my_scrabble_score.letter_points("x") == 8
    assert my_scrabble_score.letter_points("z") == 10


def test_find_score():
    assert my_scrabble_score.find_score("python") == 14
    assert my_scrabble_score.find_score("abstraction") == 15
    assert my_scrabble_score.find_score("encapsulation") == 17
    assert my_scrabble_score.find_score("inheritance") == 16
    assert my_scrabble_score.find_score("polymorphism") == 26
