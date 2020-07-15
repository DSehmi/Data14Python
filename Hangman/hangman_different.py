import hangman_brain as hl
import random as r


class Game:
    def __init__(self):
        self.user()
        self.word_completed = False
        self.__word = hl.secret_word.get_word()
        self.secret_list = []
        self.user_guess_list = []
        self.display_list = []
        self.display_list_str = ""
        self.list_view()
        self.run()

    def user(self):
        name_successful = False
        while not name_successful:
            name = input("Please enter your name\n").upper()
            if name.isalpha():
                print(f"Welcome {name} I wish you the best of luck lets start!")
                name_successful = True
            else:
                print("Please enter letters only!")
                name_successful = False
        return name

    def list_view(self):
        for letter in self.__word:
            self.secret_list.append(letter)
        for blanks in range(0, len(self.secret_list)):
            self.display_list.append("_")
            self.display_list_str = " ".join(self.display_list)
        print(self.display_list_str)

    def run(self):
        while not self.word_completed and self.lives > 0:
            user_guess = input("Guess a letter!\n").upper()
            if user_guess.isalpha() and len(user_guess) == 1:
                if user_guess in self.user_guess_list:
                    print(f"sorry you have already guessed {user_guess} please pick another letter")
                elif user_guess not in self.secret_list:
                    health_loss_rng = r.randint(1, 10)
                    self.lives = self.health(self.lives, health_loss_rng)
                else:
                    self.user_guess_list.append(user_guess)
                    index_counter = 0
                    for letter in self.secret_list:
                        if letter == user_guess:
                            self.display_list[index_counter] = letter
                        index_counter += 1
                    print(f"Horray you matched the letter {user_guess}")
                    if "_" not in self.display_list:
                        print(f"Congratulations, the word was: {self.__word}")
                        word_completed = True
                    self.display_list_str = " ".join(self.display_list)
                    print(f"{self.display_list_str}")
            else:
                print(f"sorry {user_guess} is not a letter")

new_game = Game()