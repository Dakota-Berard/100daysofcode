from tkinter import *
import pandas as pd
import random


BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = 'Arial'
current_card = {}
word_dict = {}

try:
    df = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/spanish_words.csv")
    word_dict = original_data.to_dict('records')
else:
    word_dict = df.to_dict('records')

# ---------------------------- Card Logic ------------------------------- #




def next_card():
    global current_card, flip_timer

    window.after_cancel(flip_timer)
    current_card = random.choice(word_dict)
    canvas.itemconfig(flash_text, text=current_card.get('Spanish'), fill='Black')
    canvas.itemconfig(flash_title, text="Spanish", fill='Black')
    canvas.itemconfig(canvas_img, image=flash_img)
    flip_timer = window.after(3000, func=card_flip)


def card_flip():
    canvas.itemconfig(canvas_img, image=back_img)
    canvas.itemconfig(flash_title, text='English', fill='White')
    canvas.itemconfig(flash_text, text=current_card.get('English'), fill='White')

def is_known():
    word_dict.remove(current_card)

    data = pd.DataFrame(word_dict)
    data.to_csv("data/words_to_learn.csv", index=False)


    next_card()



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=card_flip)

# Creating main Flashcard
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
flash_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
canvas_img = canvas.create_image(400, 263, image=flash_img)
flash_title = canvas.create_text(400, 150, text="Spanish", font=(FONT_NAME, 40, 'italic'))
flash_text = canvas.create_text(400, 263, text="", font=(FONT_NAME, 60, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)

# Adding buttons
x_img = PhotoImage(file="images/wrong.png")
wrong = Button(image=x_img, highlightthickness=0, command=next_card)
wrong.grid(row=1, column=0)

y_img = PhotoImage(file="images/right.png")
right = Button(image=y_img, highlightthickness=0, command=is_known)
right.grid(row=1, column=1)

window.mainloop()
