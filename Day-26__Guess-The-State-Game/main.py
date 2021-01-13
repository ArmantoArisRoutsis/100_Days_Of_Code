import turtle
import pandas

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

screen = turtle.Screen()
screen.title("U.S.A States Game")
image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


states_guessed = []
while len(states_guessed)<50:
    answer_state = screen.textinput(title=f"Guess the state({len(states_guessed)}/50 states guessed).", prompt="Guess another states name.").title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in states_guessed]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("state_to_learn.csv")
        break
    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_info = data[data.state == answer_state]
        t.goto(int(state_info.x), int(state_info.y))
        t.write(f"{answer_state}")
        states_guessed.append(answer_state)