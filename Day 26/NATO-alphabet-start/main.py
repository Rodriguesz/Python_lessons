import pandas

#TODO 1. Create a dictionary in this format:
nato_alphabet = pandas.read_csv("Day 26/NATO-alphabet-start/nato_phonetic_alphabet.csv")

alphabet = {row.iloc[0]:row.iloc[1] for(index, row) in nato_alphabet.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
running = True

while running:
    word = input("Type a word: ").upper()

    try:
        phonetic_code_list = [alphabet[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        running = False
        print(phonetic_code_list)
