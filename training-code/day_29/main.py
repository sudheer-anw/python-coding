from tkinter import *
from tkinter import messagebox
import pyperclip
import json
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!#$%&()*+'

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    Password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = Password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops!", message="Make sure to fill all the blanks")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            Password_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showwarning(title="Oops!", message="No data file found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f'Email: {email}\nPassword: {password}\n')
        else:
            messagebox.showwarning(title="Error", message=f"No details for {website} exists")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
key_image = PhotoImage(file="/home/siddique/Desktop/100 days of my couse/day_29/password-manager-start/logo.png")  # Ensure the path to your logo.png is correct
canvas.create_image(100, 100, image=key_image)
canvas.grid(row=0, column=1)

website_name_label = Label(text="Website")
website_name_label.grid(row=1, column=0)

user_name_label = Label(text="Email/Username")
user_name_label.grid(row=2, column=0)

Password_label = Label(text="Password")
Password_label.grid(row=3, column=0)

add_button = Button(text="Add", command=save, width=36)
add_button.grid(row=4, column=1, columnspan=2)

generator_button = Button(text="Generate", command=generate_password)
generator_button.grid(row=3, column=2)

search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(row=1, column=2)

# Entries
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1,)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=1)

Password_entry = Entry(width=21)
Password_entry.grid(row=3, column=1)

window.mainloop()






