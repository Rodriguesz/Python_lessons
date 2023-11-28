from tkinter import *

window = Tk()
window.title("Mile to km converter")
# window.minsize(width=350, height=100)
window.config(padx=20, pady=20)

miles_entry = Entry(width=7)
miles_entry.grid(column= 1, row= 0)


miles_label = Label()
miles_label.config(text="miles", font=("Arial", 15), padx=5)
miles_label.grid(column= 2, row= 0)



is_equal_label = Label()
is_equal_label.config(text=f"is equal to", font=("Arial", 15), padx=20)
is_equal_label.grid(column= 0, row= 1)


kilometer_result_label = Label(text="0", font=("Arial", 15))
kilometer_result_label.grid(column= 1, row= 1)


kilometer_label = Label(text="Km")
kilometer_label.grid(column= 2, row=1)


def convert():
    miles = float(miles_entry.get())
    km = miles * 1.609
    kilometer_result_label.config(text=f"{km}")
    
calculate_button = Button(text="Calculate", font=("Arial", 10), command=convert)
calculate_button.grid(column= 1, row=2)

window.mainloop()