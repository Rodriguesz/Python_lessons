from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"

#------------------READING DATA------------------#
try:
    data = pandas.read_csv("Day 31/data/words_to_learn.csv")
    print("foi")
except FileNotFoundError:
    data = pandas.read_csv("Day 31/data/french_words.csv")
    print("num foi")
finally: 
    to_learn = data.to_dict(orient="records")
    current_card = {}
    

#------------------FUNCTIONS------------------#

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card["French"].title(), fill="black")
    canvas.itemconfig(canvas_image, image=card_front_img)
    flip_timer = window.after(3000, flip_card)
    
def flip_card():
    
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"].title(), fill="white")
    canvas.itemconfig(canvas_image, image=card_back_img)
    
def words_learned():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("Day 31/data/words_to_learn.csv", index=False)
    

    next_card()
#------------------LAYOUT CONFIG------------------#
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg= BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)


canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="Day 31/images/card_front.png")
card_back_img = PhotoImage(file="Day 31/images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(column=0, row=0, columnspan=2)

card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))


wrong_button_img = PhotoImage(file="Day 31/images/wrong.png")
wrong_button = Button(image=wrong_button_img, highlightthickness=0, command= next_card)
wrong_button.grid(column=0, row=1, padx=50, pady=50)

right_button_img = PhotoImage(file="Day 31/images/right.png")
right_button = Button(image=right_button_img, highlightthickness=0, command= words_learned)
right_button.grid(column=1, row=1, padx=50, pady=50)


next_card()


window.mainloop()
