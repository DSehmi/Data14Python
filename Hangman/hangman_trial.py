import hangman_brain as hb


class Game:

    def __init__(self):
        self.secret_word = hb.secret_word.get_word()
        self.user_guess_list = []
        self.user_guesses = []
        self.play_game = True
        self.continue_game = "Y"
        self.secret_word_list = list(self.secret_word)
        self.attempts = (len(self.secret_word) + 3)

    def user(self):
        name = input("Enter your name\n")
        if name.isalpha():
            print(f"Hello {name.capitalize()}, let's play Hangman!")
        else:
            print("Please enter letters!")

    user()

    def get_guessed_letter(self):
        for letters in self.secret_word_list:
            self.user_guess_list.append("_")
        print("You have ", self.attempts, " attempts!")

    print("Your secret word is: " + ''.join(self.user_guess_list))

    get_guessed_letter()

    def guess_letter(self):
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
                Game.get_guessed_letter()
            else:
                print("Oops! Try again.")
                if self.attempts > 0:
                    print("You have ", self.attempts, " attempts left!")
                Game.get_guessed_letter()

    guess_letter()

    def win_lose(self):
        joined_list = ''.join(self.user_guess_list)
        if joined_list.upper() == self.secret_word.upper():
            print("Yay! You won.")
        elif self.attempts == 0:
            print("Too many guesses! Sorry, better luck next time.")
            print("The secret word was: " + self.secret_word.upper())

    win_lose()

    def new_game(self):
        continue_game = input("Do you want to play again? Y to continue, any other key to quit\n")
        if continue_game.upper() == "Y":
            user_guess_list = []
            user_guesses = []
            secret_word = hb.secret_word.get_new_word()
            play_game = True
        else:
            print("Thank you for playing. See you next time!")

    new_game()

