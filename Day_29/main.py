from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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

generate_button = Button(text="Generate Password", bg= "white")
generate_button.grid(column=2, row=3)

add_button = Button(text="Add Password", bg= "white", width=36)
add_button.grid(column=1, columnspan=2,  row=4)
window.mainloop()