from tkinter import *
from tkinter import messagebox
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
import random


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(numbers) for _ in range(nr_symbols)]
    password_numbers = [random.choice(symbols) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = ''.join(password_list)

    pass_entry.delete(0, END)
    pass_entry.insert(0, password)
    pyperclip.copy


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_pass():
    is_empty = True if len(web_entry.get()) < 1 or len(pass_entry.get()) < 1 else False
    is_okay = False

    if is_empty:
        messagebox.showwarning(title="Website/Password Invalid", message="Please review the information and try again")
    else:
        is_okay = messagebox.askokcancel(title=web_entry.get(),
                                         message=f"These are the details entered: \nEmail: {user_entry.get()} \nPassword: {pass_entry.get()} \nIs it correct?")

    if is_okay:
        with open("saved_passwords.txt", 'a') as file:
            file.write(f"{web_entry.get()} | {user_entry.get()} | {pass_entry.get()}\n")
        web_entry.delete(0, END)
        pass_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# textbox labels
web_label = Label(text="Website:")
web_label.grid(column=0, row=1)

user_label = Label(text="Email/Username:")
user_label.grid(column=0, row=2)

pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)

# textboxes
web_entry = Entry(width=35)
web_entry.grid(column=1, row=1, columnspan=2)
web_entry.focus()

user_entry = Entry(width=35)
user_entry.grid(column=1, row=2, columnspan=2)
user_entry.insert(0, 'example@gmail.com')

pass_entry = Entry(width=21)
pass_entry.grid(column=1, row=3, columnspan=1)

# Buttons
pass_gen = Button(text="Generate Password", command=generate_password)
pass_gen.grid(column=2, row=3)

add_pass = Button(width=36, text="Add", command=add_pass)
add_pass.grid(column=1, row=4, columnspan=2)

window.mainloop()
