window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg= BACKGROUND_COLOR)

canvas_front = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="Day 31/images/card_front.png")
canvas_front.create_image(400, 263, image=card_front_img)
canvas_front.grid(column=0, row=0, columnspan=2)

french_text = canvas_front.create_text(400, 150, text="French", font=("Arial", 40, "italic"))

word_text = canvas_front.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))


wrong_button_img = PhotoImage(file="Day 31/images/wrong.png")
wrong_button = Button(image=wrong_button_img, highlightthickness=0, command= next_card())
wrong_button.grid(column=0, row=1, padx=50, pady=50)

right_button_img = PhotoImage(file="Day 31/images/right.png")
right_button = Button(image=right_button_img, highlightthickness=0, command= next_card())
right_button.grid(column=1, row=1, padx=50, pady=50)

window.mainloop()
