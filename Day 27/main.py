from tkinter import *

window = Tk()
window.title("Testing")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


# Button
def button_click():
    my_label.config(text=input_.get())
    print("Click")


# Label
my_label = Label(text="I am a label", font=('Arial', 24))
#my_label.pack()
#my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)

# Change properties
# my_label['text'] = 'New Text'
# my_label.config(text='New Text')

button = Button(text="Click Me", command=button_click)
#button.pack()
button.grid(column=1, row=1)

# Entry
input_ = Entry(width=10)
#input_.pack()
input_.grid(column=2, row=2)

window.mainloop()
