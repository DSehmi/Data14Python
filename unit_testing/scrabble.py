# Test Driven Development!

# Write unit tests first!

# Class!
# Scrabble score calculator
# Return the score for a word according to Scrabble letter points
# Randomly generate 7 tile hand
# Check that the word can be made using those tiles
# Once a word has been made, replace only used tiles

import random


class Scrabble:

    def __init__(self):
        self.alpha = (
            "a", "b", "c", "d", "e", "f", "g", "h", "i",
            "j", "k", "l", "m", "n", "o", "p", "q", "r",
            "s", "t", "u", "v", "w", "x", "y", "z"
        )
        self.one_point = ["a", "e", "i", "l", "o", "n", "r", "s", "t", "u"]
        self.two_points = ["d", "g"]
        self.three_points = ["b", "c", "m", "p"]
        self.four_points = ["f", "h", "v", "w", "y"]
        self.five_points = ["k"]
        self.eight_points = ["j", "x"]
        self.ten_points = ["q", "z"]
        self.num_in_hand = 0
        self.hand_tiles = []
        self.selected_word = ""
        self.hand()
        self.select_word()
        self.find_score()
        self.next_turn()

    def letter_points(self, word):
        for letter in word:
            if letter in self.ten_points:
                score = 10
                return score
            elif letter in self.eight_points:
                score = 8
                return score
            elif letter in self.five_points:
                score = 5
                return score
            elif letter in self.four_points:
                score = 4
                return score
            elif letter in self.three_points:
                score = 3
                return score
            elif letter in self.two_points:
                score = 2
                return score
            else:
                score = 1
                return score

    def find_score(self):
        word_score_list = []
        for letter in self.selected_word:
            self.letter_points(letter)
            word_score_list.append(self.letter_points(letter))
        word_score = sum(word_score_list)
        print("The score for this word is: ", word_score)
        return word_score

    def hand(self):
        while self.num_in_hand < 7:
            self.tiles = random.choice(self.alpha)
            self.hand_tiles.append(self.tiles)
            self.num_in_hand += 1
        print("Your letters are", self.hand_tiles)
        return self.num_in_hand

    def select_word(self):
        valid_word = False
        while not valid_word:
            self.selected_word = input("Select a word\n")
            used_letters = []
            for letter in self.selected_word:
                used_letters.append(letter)
            if used_letters == list(filter(lambda x: x in self.hand_tiles, used_letters)):
                valid_word = True
            else:
                print("You cannot select this word")
        return self.selected_word

    def next_turn(self):
        for letter in self.selected_word:
            if letter in self.hand_tiles:
                self.tiles = random.choice(self.alpha)
                self.hand_tiles.remove(letter)
                self.hand_tiles.append(self.tiles)
        next_round = input("Would you like to go again? Press Y for Yes and any other key to exit\n").upper()
        if next_round == "Y":
            self.selected_word = ""
            self.hand()
            self.select_word()
            self.find_score()
            self.next_turn()
        else:
            print("Thank you for playing! See you next time :)")


start_game = Scrabble()
