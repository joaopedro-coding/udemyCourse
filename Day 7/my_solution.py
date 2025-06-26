# Implemented a new feature and solved a bug.
# Feature: players now can try to guess the word without having choose one letter at time.
# Bug Fixed: there's an incorrect guess tracker now. So players won't lose life while typing the same incorrect letter or answer.

import random
from hangman_words import word_list
from hangman_art import logo, stages

print(logo)

choosen_word = random.choice(word_list)
word_length = len(choosen_word)
placeholder = ""

for blank in range(word_length):
    placeholder += "_"
    
print(f"Word to guess: {placeholder}")

correct_guesses = []
incorrect_guesses = []
lives = 6
is_playing = True

while is_playing:
    guess = input("Guess a letter: ").lower()

    if guess in correct_guesses:
        print(f"You've already guessed {guess}")

    display = ""

    for letter in choosen_word:
        if guess == letter:
            display += guess
            correct_guesses.append(guess)

        elif letter in correct_guesses:
                display += letter
        else:
            display += "_"

    print(f"Word to guess: {display}")
    
    if guess not in choosen_word:
        if guess in incorrect_guesses:
            print(f"You've already guessed {guess}")
        else:
            incorrect_guesses.append(guess)
            lives -= 1
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            if lives == 0:
                print(f"***********************IT WAS {choosen_word}! YOU LOSE**********************")
                is_playing = False
        print(f"****************************{lives}/6 LIVES LEFT****************************")

    if "_" not in display or guess == choosen_word:
        is_playing = False
        print("****************************YOU WIN****************************")
    print(stages[lives])
        

print("Thanks for playing")
