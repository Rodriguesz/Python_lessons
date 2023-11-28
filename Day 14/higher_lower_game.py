from game_data import data
import random
import art
from os import system

def sort_variable():
    '''Selects two different elements from the list and returns them'''
    compare_list = random.sample(data, 2)
    return compare_list

def check_correct_answer(variable_A, variable_B):
    '''Checks if the user's answer is correct'''
    if int(variable_A["follower_count"]) > int(variable_B["follower_count"]):
        correct_answer = "A"
    else:
        correct_answer = "B"
    
    return correct_answer

def format_data(data):
    """Format account into printable format: name, description and country"""
    return f"{data["name"]}, a {data["description"]}, from {data["country"]}"


def game():
    game_running = True
    score = 0
    while game_running:
        if score == 0:
            a = sort_variable()[0]
            b = sort_variable()[1]
        else:
            a = b
            while b == a:
                b = sort_variable()[1]

        print(art.logo)

        if score >=1:
            print(f"You're right! Your current score is: {score}")

        print(f"Compare A: {format_data(a)}.")
        print(art.vs)
        print(f"Against B: {format_data(b)}.")
        answer = input("Who has more followers: Type: 'A' or 'B': ").upper()
        correct_answer = check_correct_answer(a, b)
        
        if answer == correct_answer:
            score += 1
            system("cls")
        else:
            system("cls")
            print(art.logo)
            print(f"You're wrong, sorry. Your final score is: {score}")
            game_running = False


play_again = True
while play_again:
    game()
    play_again_asnwer= input("Would you play again: 'Y' or 'N': ").upper()
    if play_again_asnwer == 'N':
        play_again = False
