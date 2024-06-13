import pandas as pd
from turtle import Turtle, Screen

screen = Screen()
turtle = Turtle()

screen.setup(500, 596)
screen.title("India State Game")
background_pic = "india_outline_map1.gif"
screen.addshape(background_pic)
turtle.shape(background_pic)

data = pd.read_csv("indian_states_coordinates.csv")
all_state = data.state.to_list()
guess_state=[]

while len(guess_state)<31:
    input_state = screen.textinput(title=f"{len(guess_state)}/50 States", prompt="What is the another state's name").title()

    if input_state in all_state:
        guess_state.append(input_state)
        t = Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == input_state]
        state_x = int(state_data.x)
        state_y = int(state_data.y)
        t.goto(state_x, state_y)
        t.write(input_state)

    if input_state == "Exit":
        missing_states = []
        for state in all_state:
            if state not in guess_state:
                missing_states.append(state)
        missing_state_data = pd.DataFrame(missing_states)
        missing_state_data.to_csv("states_to_learn.csv", index=False)
        break
