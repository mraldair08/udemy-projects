import random
import pyperclip
import json
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
    
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    
    if website_input.get() == "" or password_input.get() == "":
        messagebox.showwarning(title="WARNING", message="All fields must be fill.")
    else:
        try:
            with open ("data.json", "r") as data_file:
                #reading old data
                data = json.load(data_file) 
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #Updating old data
            data.update(new_data)              
            with open ("data.json", "w") as data_file:
                data.update(new_data)
                #Saving updated data
                json.dump(data, data_file, indent=4)
        finally:   
            website_input.delete(0,END)
            password_input.delete(0,END)
            
# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    #Obtiene info de Entry
    website = website_input.get()
    try:
        #lee el archivo 
        with open("data.json") as file:
            #guarda data.json en variable data para consultar
            data = json.load(file)
    except FileNotFoundError:
        #si no se ha creado el archivo muestra error
        messagebox.showinfo(title="Data Not Found", message="No data file found.")
    else:
        #busca el website dentro de los registros de data
        if website in data:
            #Se seleccionan los valores asignados al website seleccionado
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title="Information", message=f"Email: {email}\n Password: {password}")
        else:
            messagebox.showinfo(title="Data not found", message=f"{website} nof found on file")

            
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg= "white" )

canvas = Canvas(width=200, height=200, highlightthickness=0, bg= "white")
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

#Labels
website_label = Label(text="Website:", font=("calibri", 12, "italic"), bg= "white")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:", font=("calibri", 12, "italic"), bg= "white")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:", font=("Calibri", 12, "italic"), bg= "white")
password_label.grid(column=0, row=3)

#Entries
website_input = Entry(width=21)
website_input.grid(column=1,  row=1)
website_input.focus()
email_input = Entry(width=35)
email_input.insert(0, "aldair.cerezo@ocsassist.com")
email_input.grid(column=1,columnspan=2,  row=2)
password_input = Entry(width=21)
password_input.grid(column=1,  row=3)

#Buttons
search_button = Button(text="Search", bg= "white", command=find_password)
search_button.grid(column=2, row=1)
generate_button = Button(text="Generate Password", bg= "white", command=generate_password)
generate_button.grid(column=2, row=3)
add_button = Button(text="Add Password", bg= "white", width=36, command=save)
add_button.grid(column=1, columnspan=2,  row=4)

window.mainloop()