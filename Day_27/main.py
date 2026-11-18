#import tkinter
from tkinter import *


def button_click():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

window = Tk()
window.title("My first GUI")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

#label
my_label = Label(text="I am a Label", font=("Arial", 25, "italic"))
my_label.config(text="New text")
#my_label.pack()
#my_label.place(x=30, y=200)
my_label.grid(column=0, row=0)
my_label.config(padx=20, pady=20)

#button
button = Button(text="Click me", command=button_click)
button.grid(column=1, row=1)



new_button = Button(text="Click 2", command=button_click)
new_button.grid(column=2, row=0)

#Entry
input = Entry(width=10)
input.grid(column=3, row=3)






window.mainloop()