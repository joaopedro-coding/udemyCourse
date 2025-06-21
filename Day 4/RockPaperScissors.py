import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

possible_moves = [rock, paper, scissors]
player_move_num = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if not 0 <= player_move_num <= 2:
    print("You picked an invalid number. You lose.")
else:
    print(possible_moves[player_move_num])
player_move = possible_moves[player_move_num]

computer_move_num = random.randint(0,2)
computer_move = possible_moves[computer_move_num]
print("Computer choose:")
print(possible_moves[computer_move_num])

if player_move == computer_move:
    print("It's a tie")
elif player_move == rock and computer_move == scissors:
    print("You win")
elif player_move == paper and computer_move == rock:
    print("You win")
elif player_move == scissors and computer_move == paper:
    print("You win")
else:
    print("You lose")
