import turtle
import pandas

# Set up screen
screen = turtle.Screen()
screen.title("U.S. State Guessing Game")
image = "training-code/day_26/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Read CSV file
data = pandas.read_csv("training-code/day_26/day_26/50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()
    
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state is not guessed_states]
        # for state in all_states:
        #     if state is not guessed_states:
        #         missing_states.append(state)
        print(missing_states)
        break
    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        state_data = data[data.state == answer_state]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)

    



    






