import turtle
import pandas

TOTAL_STATES = 50
FONT = ("Courier", 15, "normal")

# Screen config
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "Day 25/final project/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

state = turtle.Turtle()
state.hideturtle()
state.penup()

#reading csv file
data = pandas.read_csv("Day 25/final project/50_states.csv")

text = "Type an state"
correct_states = []

while len(correct_states) < 50:
    answer_state = screen.textinput(title= f"{len(correct_states)}/50 Guess the State", prompt=text).title()
    # se o usuario digitar exit
    if answer_state == "Exit":
        missing_states = []
        for state in data.state:
            if state not in correct_states:
                missing_states.append(state)
        data_dict = {
                "States": missing_states,
            }
        #cria uma aquivo com os estados que não foram digitados
        missing_states_data = pandas.DataFrame(data_dict)
        missing_states_data.to_csv("Day 25/final project/states_to_learn.csv")
        break
    else:
        try:
            #tenta pegar os dados do estado caso tenha digitado o estado corretamente
            get_state_data = data[data.state == answer_state]
            state_xcor = int(get_state_data["x"].iloc[0])
            state_ycor = int(get_state_data["y"].iloc[0])
            state.goto(state_xcor, state_ycor)
            state.write(arg=answer_state, align= "center", font= FONT, move= False)
            text = "What's another state's name? (Type 'exit' if you want to close this window)"
            correct_states.append(answer_state)
        except:
            #caso contrario, muda do texto do input para 'Wrong state!'
            text = "Wrong state! (Type 'exit' if you want to close this window)"
            



screen.mainloop()
