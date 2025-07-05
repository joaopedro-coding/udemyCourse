from art import logo
import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def count_cards(hand):
    if sum(hand) == 21 and len(hand) == 2:
        return 0
    
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)

    return sum(hand)

def evaluate_result(p_score, c_score):
    if p_score == c_score:
        return "Draw 😊"
    elif c_score == 0:
        return "You lost. Opponent has a blackjack 😱 "
    elif p_score == 0:
        return "Win with a blackjack 😎"
    elif c_score > 21:
        return "Opponent went over. You win 😝"
    elif p_score > 21:
        return "You went over. You lost 🥲"
    elif p_score > c_score:
        return "You win 😁"
    else:
        return "You lost 😑"

def play_game():
    print(logo)
    player_hand = []
    computer_hand = []
    player_score = -1
    computer_score = -1
    is_playing = True

    for _ in range(2):
        player_hand.append(deal_card())
        computer_hand.append(deal_card())

    while is_playing:
        
        player_score = count_cards(player_hand)
        computer_score = count_cards(computer_hand)

        print(f"Your cards: {player_hand}, current score: {player_score}")
        print(f"Computer's first card: {computer_hand[0]}")

        if player_score == 0 or computer_score == 0 or player_score > 21:
            is_playing = False
        else:
            continue_dealing = input("Type 'y' to get another card or 'n' to pass: ")
            if continue_dealing == "y":
                player_hand.append(deal_card())
            else:
                is_playing = False

    while computer_score != 0 and computer_score < 17:
        computer_hand.append(deal_card())
        computer_score = count_cards(computer_hand)

    print(f"Your final hand: {player_hand}, final score: {player_score}")
    print(f"Computer's final hand: {computer_hand}, final score: {computer_score}")
    print(evaluate_result(player_score, computer_score))
            
want_to_play = True
while want_to_play:
    keep_playing = input("Do you want to play a game of blackjack? Type 'y' to yes or 'n' to no: ")
    if keep_playing == 'y' or keep_playing == 'yes':
        print("\n" * 20)
        play_game()
    elif keep_playing == 'n' or play_game == 'no':
        want_to_play = False
    else:
        print("Please choose a valid option")
