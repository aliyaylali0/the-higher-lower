from art import logo,vs
from game_data import data
import random
from replit import clear

def format_data(player):
    player_name = player['name']
    player_description = player['description']
    player_country = player['country']
    return f"{player_name}, a {player_description}, from {player_country}"


def check(your_choice, player_1_number,player_2_number):
    if player_1_number > player_2_number:
        return your_choice == 'a'
    else:
        return your_choice == 'b'


score = 0
print(logo)

game_loop = True
player_2 = random.choice(data)
while game_loop:

    player_1 = player_2
    player_2 = random.choice(data)


    if player_2 == player_1:
        player_2 = random.choice(data)

    print(f"Compare_A: {format_data(player_1)}")
    print(vs)
    print(f"Against_B: {format_data(player_2)}")

    your_choice = input("Higher or Lower (A or B): ").lower()


    player_1_number = player_1['follower_count']
    player_2_number = player_2['follower_count']

    is_correct = check(your_choice,player_1_number,player_2_number)

    clear()

    if is_correct:
        score += 1
        print(f"Well Done! Your Score {score}")
    else:
        print("game over")
        print(f"Score: {score}")
        game_loop = False
