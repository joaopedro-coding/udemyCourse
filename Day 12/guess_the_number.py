from random import randint
from art import logo

EASY_DIFFICULTY = 10
HARD_DIFFICULTY = 5

def choose_number():
    return randint(1,100)

def calculate_atempts():
    difficulty = ""
    while difficulty not in ["easy", "hard"]:
        difficulty = input("Choose your dificulty. Type 'easy' or 'hard': ")
        if difficulty == "easy":
            return EASY_DIFFICULTY
        elif difficulty == "hard":
            return HARD_DIFFICULTY
    
def resolve(guess, random_num, attempts, num_of_tries):
    if guess > random_num:
        print("Too high")
        return attempts - 1
    elif guess < random_num:
        print("Too low")
        return attempts - 1
    elif guess == random_num and num_of_tries == 1:
        print("Nice, right away!")
    else:
        print(f"You got it. Well done. You took {num_of_tries} attempts")

def play_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    random_number = choose_number()
    print(random_number)
    
    number_of_attempts = calculate_atempts()
    guess = 0
    tries = 0

    while guess != random_number:
        print(f"You have {number_of_attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        tries += 1
        number_of_attempts = resolve(guess, random_number, number_of_attempts, tries)

        if number_of_attempts == 0:
            print("You've run out of guesses. Try again.")
            return
        elif guess != random_number:
            print("Guess again.")

play_game()
is_playing = True
while is_playing:
    play_again = input("Do you want to play again? Type 'y' or 'n': ")

    if play_again == "n":
        print("Thanks for playing")
        is_playing = False
    elif play_again == "y":
        print("\n" * 20)
        play_game()
    else:
        print("Please choose a valid option.")
