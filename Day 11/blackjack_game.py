from art import logo
import random
from os import system
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

def player_score_count(player_score, player_cards):
    player_score = 0
    for card in range(len(player_cards)):
        player_score += player_cards[card]
    return player_score

def computer_score_count(computer_score, computer_cards):
    computer_score = 0
    for card in range(len(computer_cards)):
        computer_score += computer_cards[card]
    return computer_score

def blakcjack():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    
    player_cards = []
    computer_cards =[]
    player_score = 0
    computer_score = 0

    for _ in range(2):
        player_cards.append(random.choice(cards))
    computer_cards = [random.choice(cards)]

    player_score = player_score_count(player_score, player_cards)
    print(f'Your cards: {player_cards}, current score: {player_score}')
    print(f"Computer's firs card: {computer_cards}")

    picking_cards = True
    while picking_cards and player_score <= 21:
        another_card = input("Type 'y' to get another card, type 'n' to pass: " )
        if(another_card == 'y'):
            player_cards.append(random.choice(cards))
            player_score = player_score_count(player_score, player_cards)
            print(f'Your cards: {player_cards}, current score: {player_score}')
            print(f"Computer's firs card: {computer_cards}")
        else:
            picking_cards = False

    if(player_score <= 21):
        while computer_score <= 21 and computer_score < player_score:
            computer_cards.append(random.choice(cards))
            computer_score = computer_score_count(computer_score, computer_cards)
    else:
            computer_score = computer_score_count(computer_score, computer_cards)

    system('cls')

    print(f"Your final hand: {player_cards}, final score: {player_score}")
    print(f"Computer's final hando: {computer_cards}, final score: {computer_score}")

    if(player_score > computer_score):
        if(player_score <= 21):
            print("Congrats! you win.")
        else:
            print("Oh no! you lose :(")
    elif(computer_score > player_score):
        if(computer_score <= 21):
            print("Oh no! you lose :(")
        else:
            print("Congrats! you win.")
    else:
        print("Draw!")
    


game_running = True
while game_running:
    answer = input("Start Blackjack? 'y' or 'n': ")
    if(answer == 'n'):
            print("Thanks for playing blackjack game :)")
            game_running = False
    else:
        system('cls')
        print(logo)        
        blakcjack()