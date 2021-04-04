import random


def play():
    user_move = input("'r' for rock, 'p' for paper, 's' for scissors: ")
    computer_move = random.choice(('r', 'p', 's'))
    checkwinner(user_move, computer_move)


def checkwinner(player1, player2):
    scenario = f"{player1} vs {player2}"
    print(f"{scenario}")
    if player1 == player2:
        print("Draw!")
    elif ((player1 == 'r') and (player2 == 's')) \
            or ((player1 == 'p') and (player2 == 'r')) \
            or ((player1 == 's') and (player2 == 'p')):
        print("Player 1 wins!")
    elif ((player2 == 'r') and (player1 == 's')) \
            or ((player2 == 'p') and (player1 == 'r')) \
            or ((player2 == 's') and (player1 == 'p')):
        print("Player 2 wins!")

play()