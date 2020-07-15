import hangman_brain as hb


class Game:

    def __init__(self):
        self.user()
        self.secret_word = hb.secret_word.get_word()
        self.user_guess_list = []
        self.user_guesses = []
        self.secret_word_list = list(self.secret_word)
        self.attempts = (len(self.secret_word) + 3)
        self.get_guessed_letter()
        self.view()
        self.run()

    def user(self):
        name = input("Please enter your name\n")
        print(f"Hello {name.capitalize()}, let's play Hangman!")

    def get_guessed_letter(self):
        return "Your secret word is: " + ''.join(self.user_guess_list)

    def view(self):
        for letter in self.secret_word_list:
            self.user_guess_list.append("_")
        print(self.get_guessed_letter())
        print("You have ", self.attempts, " attempts remaining!")

    def run(self):
        while True:
            letter = input("Guess a letter:\n").upper()

            if letter in self.user_guesses:
                print("You already guessed this letter, try something else.")

            else:
                self.attempts -= 1
                self.user_guesses.append(letter)
                if letter in self.secret_word_list:
                    print("Nice guess!")
                    if self.attempts > 0:
                        print("You have ", self.attempts, " attempts left!")
                    for i in range(len(self.secret_word_list)):
                        if letter == self.secret_word_list[i]:
                            letter_index = i
                            self.user_guess_list[letter_index] = letter.upper()
                    print(self.get_guessed_letter())
                else:
                    print("Oops! Try again.")
                    if self.attempts > 0:
                        print("You have ", self.attempts, " attempts left!")
                    print(self.get_guessed_letter())

            joined_list = ''.join(self.user_guess_list)
            if joined_list.upper() == self.secret_word.upper():
                print("Yay! Congratulations, you won.")
                break
            elif self.attempts == 0:
                print("You have run out of guesses! Sorry, better luck next time.")
                print("The secret word was: " + self.secret_word)
                self.new_game()
                break

    def play_new_game(self):
        self.secret_word = hb.secret_word.get_new_word()
        return self.secret_word

    def new_game(self):
        continue_game = input("Do you want to play again? Y to continue, any other key to quit\n")
        if continue_game.upper() == "Y":
            self.play_new_game()
        else:
            print("Thank you for playing. See you next time!")


run_game = Game()
