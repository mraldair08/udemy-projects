from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    klilometer = miles * 1.609
    kilometer.config(text=f"{klilometer}")

window = Tk()
window.title("My first GUI")
#window.minsize(width=100, height=300)
window.config(padx=20, pady=20)


miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles", font=("Arial", 25, "italic"))
miles_label.grid(column=2, row=0)

miles = Label(text="Miles", font=("Arial", 25, "italic"))
miles.grid(column=2, row=0)

is_equal = Label(text="is equal to", font=("Arial", 25, "italic"))
is_equal.grid(column=0, row=1)

kilometer = Label(text="0", font=("Arial", 25, "italic"))
kilometer.grid(column=1, row=1)

km = Label(text="Km", font=("Arial", 25, "italic"))
km.grid(column=2, row=1)

button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)

window.mainloop()