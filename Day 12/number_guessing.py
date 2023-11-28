# TODO LIST
# GERAR UM NÚMERO ALEATÓRIO DE 1 A 100
# PERGUNTAR A DIFICULDADE
# MUDAR O NÚMERO DE TENTATIVAS DE ACORDO COM A DIFICULDADE (EASY = 10, HARD = 5)
# INFORMAR O USUARIO SE O NÚMERO DIGITADO É MAIOR OU MENOR Q O NÚMERO ESCOLHIDO
# INFORMAR QUANTAS TENTATIVAS AINDA RESTAM
# INFORMAR O USUARIO SE ELE GANHOU
# OU INFORMAR O USUARIO SE ELE PERDEU CASO ACABEM AS TENTATIVAS E ELE NÃO TENHA ACERTADO

#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from art import logo

# Generating a int number between 1 and 100
chosen_number = random.randint(1, 100)

print(logo)
print("Welcome to the number Guessing Game!")
print("I'm thinking of a number between 1 and 100. Can you guess it?")

# Asking the user the difficulty they want
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == 'easy':
    lifes = 10
elif difficulty == 'hard':
    lifes = 5

print(f"You have {lifes} lifes. Good lucky!")


# Repeat the guessing functionality if they get it wrong and if he has lives left
guess = 0
while lifes >= 1 and guess != chosen_number:
    guess = int(input("Type a number: "))
    if guess != chosen_number: 
        if guess > chosen_number:
            print("Too high. Try again!")
        else:
            print("Too low. Try again!")
        lifes -= 1
        print(f"You have {lifes} left.")

# if he is correct
if guess == chosen_number:
    print("You win. Congrats!")
# if he didn't guess the number
else:
    print(f"The number is {chosen_number}")
    print("You failed, my friend. Good lucky next time!")
