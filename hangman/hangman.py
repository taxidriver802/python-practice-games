import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words) # randomly select a word from the list
    while "-" in word or " " in word:
        word = random.choice(words) # select a new word if the selected word contains "-" or " "
    return word.upper() # return the selected word in uppercase

def hangman():
    wins = 0  # Initialize the win counter

    while True:  # Loop to allow replaying the game
        word = get_valid_word(words)  # Get a valid word
        word_letters = set(word)  # Letters in the word
        alphabet = set(string.ascii_uppercase)  # All letters in the alphabet
        used_letters = set()  # Letters that have been guessed
        
        lives = 6  # Number of lives the player has
        if len(word) > 6:
            lives = 8 # Increase lives for longer words

        while word_letters and lives > 0:
            # Display used letters, current word, and remaining lives
            print(f"You have {lives} lives left and have used these letters: {' '.join(used_letters)}")
            print(f"Current word: {' '.join([letter if letter in used_letters else '-' for letter in word])}")

            # Get user input
            user_letter = input("Guess a letter: ").upper()

            # Process user input
            if user_letter in alphabet - used_letters:
                used_letters.add(user_letter)
                if user_letter in word_letters:
                    word_letters.remove(user_letter)
                    print(f"Good guess! '{user_letter}' is in the word.")
                else:
                    lives -= 1  # Decrease lives for a wrong guess
                    print(f"'{user_letter}' is not in the word. You lose a life.")
            elif user_letter in used_letters:
                print(f"You have already used '{user_letter}'. Try again.")
            else:
                print(f"'{user_letter}' is not a valid letter. Please try again.")

        # End of game
        if lives == 0:
            print(f"Game over! You ran out of lives. The word was: {word}")
        else:
            print(f"Congratulations! You guessed the word: {word}")
            wins += 1  # Increment the win counter
            print(f"Your current win streak is: {wins}")

        # Ask if the player wants to play again
        play_again = input("Do you want to play again? (Y/N) ").upper()
        if play_again != "Y":
            print(f"Thanks for playing! Your total wins: {wins}")
            break

user_input = input("Do you want to play Hangman? (Y/N) ").upper()
if user_input == "Y":
    hangman()
else:
    print("Goodbye!")