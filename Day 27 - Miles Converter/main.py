from tkinter import *

window = Tk()
window.title("Mile to Kilometer Converter")
window.minsize(width=250, height=150)
window.config(padx=20, pady=20)


# Button
def button_click():
    new_text = int(input_.get()) * 1.6
    answer.config(text=new_text)
    print("Click")


# Label
equal_to = Label(text="is equal to", font=('Arial', 12))
#my_label.pack()
#my_label.place(x=0, y=0)
equal_to.grid(column=0, row=1)

miles = Label(text=" Miles", font=('Arial', 12))
#my_label.pack()
#my_label.place(x=0, y=0)
miles.grid(column=2, row=0)

kilometers = Label(text="Km", font=('Arial', 12))
#my_label.pack()
#my_label.place(x=0, y=0)
kilometers.grid(column=2, row=1)

answer = Label(text="0", font=('Arial', 12))
#my_label.pack()
#my_label.place(x=0, y=0)
answer.grid(column=1, row=1)

# Change properties
# my_label['text'] = 'New Text'
# my_label.config(text='New Text')

button = Button(text="Calculate", command=button_click)
#button.pack()
button.grid(column=1, row=3)

# Entry
input_ = Entry(width=10)
#input_.pack()
input_.grid(column=1, row=0)

window.mainloop()
