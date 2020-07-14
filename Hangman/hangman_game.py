# hangman 'game' class:
#   handle game logic
#   get guesses off the player
#   keeps track of the score


# class Game:
#
#     def __init__(self):
#         self.word_length = len(secret_word)
#         self.lives = len(secret_word) + 3

import hangman_brain as hb

secret_word = hb.secret_word.get_word()

user_guess_list = []
user_guesses = []
play_game = True
continue_game = "Y"

name = input("Enter your name\n")
print(f"Hello {name.capitalize()}, let's play Hangman!")

while True:

    if play_game:

        secret_word_list = list(secret_word)
        attempts = (len(secret_word) + 3)

        def get_guessed_letter():
            print("Your secret word is: " + ''.join(user_guess_list))

        for letter in secret_word_list:
            user_guess_list.append("_")
        get_guessed_letter()

        print("You have ", attempts, " attempts!")

        while True:

            letter = input("Guess a letter:\n").upper()

            if letter in user_guesses:
                print("You already guessed this letter, try something else.")

            else:
                attempts -= 1
                user_guesses.append(letter)
                if letter in secret_word_list:
                    print("Nice guess!")
                    if attempts > 0:
                        print("You have ", attempts, " attempts left!")
                    for i in range(len(secret_word_list)):
                        if letter == secret_word_list[i]:
                            letter_index = i
                            user_guess_list[letter_index] = letter.upper()
                    get_guessed_letter()
                else:
                    print("Oops! Try again.")
                    if attempts > 0:
                        print("You have ", attempts, " attempts left!")
                    get_guessed_letter()

            joined_list = ''.join(user_guess_list)
            if joined_list.upper() == secret_word.upper():
                print("Yay! You won.")
                break
            elif attempts == 0:
                print("Too many guesses! Sorry, better luck next time.")
                print("The secret word was: " + secret_word.upper())
                break

        continue_game = input("Do you want to play again? Y to continue, any other key to quit\n")
        if continue_game.upper() == "Y":
            user_guess_list = []
            user_guesses = []
            secret_word = hb.secret_word.get_new_word()
            play_game = True
        else:
            print("Thank you for playing. See you next time!")
            break
    else:
        break



