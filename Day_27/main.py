import tkinter

window = tkinter.Tk()

window.title("My first GUI")
window.minsize(width=500, height=300)

#label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 25, "italic"))
my_label.pack()







window.mainloop()