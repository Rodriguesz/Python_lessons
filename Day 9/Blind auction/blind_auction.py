from logo import logo
from os import system

def finding_winner(bidders):
    winner = {"name": "", "bid": 0}
    for bidder in bidders:
        print(bidder)
        if bidder["bid"] > winner["bid"]:
            winner["name"] = bidder["name"]
            winner['bid'] = bidder["bid"]
    print(f"the winner is {winner['name']} with a bid of ${winner['bid']}.")
        

print(logo)

answer = 'yes'
bidders = []

while answer == 'yes':
    print("Welcome to the secret auction program.")
    name = input("What's your name?: ")
    bid = float(input("What's your bid?: "))
    answer = input("Are there other bidders? yes or no: ")
    bidders.append({"name": name, "bid": bid})
    system("cls")

finding_winner(bidders= bidders)