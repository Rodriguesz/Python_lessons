from art import logo
from os import system
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def div(a, b):
    return a / b

def mult(a, b):
    return a * b



print(logo)

running = True

first_number = float(input("First number: "))
while running:    
    operation = input("ADD (+)\nSUB (-)\nDIV (/)\nMult (*)\nChoose an operation: ")
    second_number = float(input("Second number: "))

    if operation == '+':
        result = add(first_number, second_number)
    elif operation == '-':
        result = sub(first_number, second_number)
    elif operation == '/':
        result = div(first_number, second_number)
    elif operation == '*':
        result = mult(first_number, second_number)
    else:
        print("invalid operation")
    
    print(f"{first_number}{operation}{second_number} = {result}")
    answer = input(f"You want to do another operation with {result}? Y or N: ")
    if answer != 'y':
        running = False
    else:
        first_number = result
        system('cls')
    
print('Vai-te embora carniça')
