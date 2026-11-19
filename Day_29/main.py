import random
import pyperclip
from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
#Save password
def save():
    
    if website_input.get() == "" or password_input.get() == "":
        messagebox.showwarning(title="WARNING", message="All fields must be fill.")
    else:
        is_ok = messagebox.askokcancel(title=f"{website_input.get()}", message=f"There are the details entered: \nEmail: {email_input.get()}\nPassword: {password_input.get()}\nIs it ok to save?")
        
        if is_ok:
            with open ("data.txt", "a") as f:
                f.write(f"{website_input.get()} | {email_input.get()} | {password_input.get()}\n")
            website_input.delete(0,END)
            password_input.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg= "white" )

canvas = Canvas(width=200, height=200, highlightthickness=0, bg= "white")
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", font=("calibri", 12, "italic"), bg= "white")
website_label.grid(column=0, row=1)
website_input = Entry(width=35)
website_input.grid(column=1,columnspan=2,  row=1)
website_input.focus()

email_label = Label(text="Email/Username:", font=("calibri", 12, "italic"), bg= "white")
email_label.grid(column=0, row=2)
email_input = Entry(width=35)
email_input.insert(0, "aldair.cerezo@ocsassist.com")
email_input.grid(column=1,columnspan=2,  row=2)

password_label = Label(text="Password:", font=("Calibri", 12, "italic"), bg= "white")
password_label.grid(column=0, row=3)
password_input = Entry(width=21)
password_input.grid(column=1,  row=3)

generate_button = Button(text="Generate Password", bg= "white", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add Password", bg= "white", width=36, command=save)
add_button.grid(column=1, columnspan=2,  row=4)
window.mainloop()