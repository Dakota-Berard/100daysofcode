from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
checkmark_str = ''


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    global checkmark_str
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    checkmark.config(text="")
    checkmark_str = ''
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = 5  # WORK_MIN * 60
    short_break_sec = 5  # SHORT_BREAK_MIN * 60
    long_break_sec = 5  # LONG_BREAK_MIN * 60

    if reps % 2 == 1:
        timer_label.config(text="Working", fg=GREEN)
        count_down(work_sec)
    elif reps % 8 == 0:
        timer_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
    else:
        timer_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps
    global checkmark_str
    count_minutes = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = "0" + str(count_seconds)

    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            checkmark_str += "✓"
            checkmark.config(text=checkmark_str)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
# window.minsize(height=600, width=600)
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Text and buttons
timer_label = Label(text="Timer", font=(FONT_NAME, 48, 'normal'), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

start_button = Button(text='Start', font=(FONT_NAME, 10, 'normal'), command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text='Reset', font=(FONT_NAME, 10, 'normal'), command=reset_timer)
reset_button.grid(column=2, row=2)

checkmark = Label(font=(FONT_NAME, 20, 'normal'), fg=GREEN, bg=YELLOW)
checkmark.grid(column=1, row=3)

window.mainloop()
