#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
        

with open("Day_24/Mail Merge Project Start/Input/Letters/starting_letter.txt") as file:
    letter = file.read()
   
with open("Day_24/Mail Merge Project Start/Input/Names/invited_names.txt") as file:
    guests = file.readlines()
    
old_guest = "[name]"
for guest in guests:
    guest_name = guest.strip("\n")
    new_letter = letter.replace(old_guest, guest_name)
    
    with open(f"Day_24/Mail Merge Project Start/Output/ReadyToSend/letter_for_{guest_name}.txt", mode="w") as completed_letter:
        completed_letter.write(new_letter)

    