import turtle
import pandas

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.setup(width=800, height=600)

tim = turtle.Turtle()
tim.penup()
tim.hideturtle()


data = pandas.read_csv("50_states.csv")
guessed_states = []
all_states = data.state.to_list()
title_string = "Guess the State"

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=title_string, prompt="What's another state's name?").title()
    if answer_state == "Quit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in data.values:
        guessed_states.append(answer_state)
        title_string = f"{len(guessed_states)}/50 States Correct"
        state = data[data.state == answer_state]
        tim.goto(int(state.x), int(state.y))
        tim.write(answer_state, font=("Comic Sans", 8, "normal"))


