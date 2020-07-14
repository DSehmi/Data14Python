# hangman 'brain' class:
#   knows the word to guess
#   and has methods to return information about the word

from hangman_words import word_list
import random as r


class Brain:

    def __init__(self):
        self.word = r.choice(word_list)

    def get_word(self):
        return self.word.upper()

    def get_new_word(self):
        new_word = r.choice(word_list)
        if self.word == secret_word:
            new_word = r.choice(word_list)
        return new_word


secret_word = Brain()
