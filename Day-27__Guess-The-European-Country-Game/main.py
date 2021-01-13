import turtle
import pandas

data = pandas.read_csv("countries.csv")
all_states = data.state.to_list()

screen = turtle.Screen()
screen.setup()
screen.title("U.S.A States Game")
image = "./europe_map.gif"
screen.addshape(image)
turtle.shape(image)

# def get_click(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_click)
# turtle.mainloop()

country_guessed = []
while len(country_guessed)<37:
    answer_country = screen.textinput(title=f"({len(country_guessed)}/37 countries guessed).", prompt="Guess Another Country ").title()

    if answer_country == "Exit":
        missing_countries = []
        for i in all_states:
            if i not in country_guessed:
                missing_countries.append(i)
        new_data = pandas.DataFrame(missing_countries)
        new_data.to_csv("countries_to_learn.csv")
        break
    if answer_country in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_info = data[data.state == answer_country]
        t.goto(int(state_info.x), int(state_info.y))
        t.write(f"{answer_country}",align="center",font=("Arial",7,"bold"))
        country_guessed.append(answer_country)

