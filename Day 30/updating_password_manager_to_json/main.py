from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ------------------------------ SEARCH WEBSITE --------------------------------- #
def find_password():
    website = website_entry.get().title()
    try:
        with open("Day 30/updating_password_manager_to_json/my_passwords.json", mode= "r") as data_file:
            #Reading old data
            data = json.load(data_file)
            email = data[website]["email"]
            password = data[website]["password"]
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No existing file")
    except KeyError:
        messagebox.showinfo(title="Error", message=f"No details for the {website} exists")
    else: 
        messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")

        
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)


    #letters
    password_letters = [random.choice(letters) for _ in range(nr_letters)]

    #symbols
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    #numbers
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)
    password = "".join(password_list)
    
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():
    website = website_entry.get().title()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    
    if website == "" or email == "" or password == "":
        messagebox.showinfo(title="Ooops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("Day 30/updating_password_manager_to_json/my_passwords.json", mode= "r") as data_file:
                #Reading old data
                data = json.load(data_file)
                
        except FileNotFoundError:
            with open("Day 30/updating_password_manager_to_json/my_passwords.json", mode= "w") as data_file:
                #saving updated data
                json.dump(new_data, data_file, indent=4)
                
        else:
            #Updating old data with new data
            data.update(new_data)
            
            with open("Day 30/updating_password_manager_to_json/my_passwords.json", mode= "w") as data_file:
                #saving updated data
                json.dump(data, data_file, indent=4)
                
        finally:        
            website_entry.delete(0, END)
            password_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="Day 30/updating_password_manager_to_json/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row= 0)


website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry(width=32)
website_entry.grid(column=1, row=1)
website_entry.focus()

search_button = Button(text="Search", width=14, command= find_password)
search_button.grid(column=2, row=1)

user_label = Label(text="Email/Username:")
user_label.grid(column=0, row=2)

email_entry = Entry(width=51)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "venom.extreme682@gmail.com")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=32)
password_entry.grid(column=1, row=3)

password_generator_button = Button(text= "Generate Password", command=generate_password)
password_generator_button.grid(column=2, row=3)

add_button = Button(text= "ADD", width=44, command=save_pass)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
