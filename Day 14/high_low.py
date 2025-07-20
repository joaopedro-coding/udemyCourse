from random import choice
from game_data import data
from art import logo, vs

def print_data(famous_data, key):
    print(f"Compare {key}: {famous_data["name"]}, a {famous_data["description"]}, from {famous_data["country"]}")

def pick_famous():
    famous_random_data = choice(data)
    data.remove(famous_random_data) 
    return famous_random_data

def check_answer(user_guess, account_a, account_b):
    if account_a > account_b:
        return user_guess == "A"
    elif account_b > account_a:
        return user_guess == "B"

def play_game():
    data_a = pick_famous()
    data_b = pick_famous()
    score = 0

    is_playing = True

    while is_playing:
        print(logo)
        print_data(data_a, "A")
        print(vs)
        print_data(data_b, "B")

        key_input = input("Who has more followers? Type 'A' or 'B': ").upper()
        print("\n" * 20)

        is_correct_answer = check_answer(key_input, data_a["follower_count"], data_b["follower_count"])

        if is_correct_answer:
            score += 1
            data_a = data_b
            data_b = pick_famous()
            print(f"You're right! Current score: {score}.")
        else:
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}.")
            is_playing = False
    
    play_again = input("Do you want to play again? ")
    if play_again == "y":
        print("\n" * 20)
        play_game()
    else:
        print("Thanks for playing!")
play_game()
