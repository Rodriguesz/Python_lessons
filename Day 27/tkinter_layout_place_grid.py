from tkinter import * 

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Label
label = Label(text="I am a label", font=("Arial", 24, "italic"))
#? PLACE
# label.place(x=100, y=200)

#? GRID
label.grid(column=0, row= 0)

label["text"] = "new text"
label.config(text = "New Text", padx=50, pady=20)


#Button
def button_clicked():
    label.config(text=input_field.get())

button = Button(text = "click me", command=button_clicked)
button.grid(column=1, row=2)

new_button = Button(text = ("new button"))
new_button.grid(column=2, row=0)

#Entry
input_field = Entry(width= 10)
input_field.grid(column=3, row=3)

window.mainloop()