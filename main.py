import turtle
import pandas

screen = turtle.Screen()
screen.setup(width=700, height=1000)
screen.title("Distritos de Portugal")
image = "mapa_de_portugal.gif"
screen.addshape(image)
turtle.shape(image)
score = 0
data = pandas.read_csv("distritos_portugal.csv")
all_states = data.distrito.to_list()
answers = []


while len(answers) < 18:
    answer_state = (screen.textinput(title=f"{score}/18 Guess The State", prompt="What's another state's name?")
                    .title())
    if answer_state == "Exit":
        missing_states = [state for state in all_states if (state not in answers)]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("distritos_faltam.csv")
        break

    if answer_state in all_states:
        # print(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        distrito_data = data[data.distrito == answer_state]
        t.goto(int(distrito_data.x.iloc[0]), int(distrito_data.y.iloc[0]))
        t.write(answer_state)
        score += 1
        answers.append(answer_state)
