import turtle
import pandas

# Set up screen
screen = turtle.Screen()
screen.title("india. State Guessing Game")
image = "MAP.PY/india.gif"
screen.addshape(image)
turtle.shape(image)

# Read CSV file
data = pandas.read_csv("MAP.PY/ind_state_coo.csv")
all_state = data.state.to_list()
guessed_State = []

while len(guessed_State) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_State)}/50 States Correct", prompt="What's another state's name?").title()
    
    if answer_state == "Exit":
        missing_states = []
        for state in all_state:
            if state is not guessed_State:
                missing_states.append(state)
        print(missing_states)
        break
    if answer_state in all_state and answer_state not in guessed_State:
        guessed_State.append(answer_state)
        state_data = data[data.state == answer_state]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(state_data.Latitude.item(), state_data.Longitude.item())
        t.write(answer_state)




