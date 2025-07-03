import turtle
import pandas

# Set up the screen
screen = turtle.Screen()
screen.title("Desi Map Hunt")
image = "Map.gif"
screen.addshape(image)
turtle.shape(image)

# Load state data
data = pandas.read_csv("28_States.csv")
stateNames = data["states"].to_list()
guessedStates = []
Counter = 0

# Main loop
while len(guessedStates) < 28:
    AnswerState = turtle.textinput(f"({Counter}/28)Guess The State!", prompt="What is your Guess?").title()
    AnswerState.title()

    # Correct guess
    if AnswerState in stateNames and AnswerState not in guessedStates:
        guessedStates.append(AnswerState)
        Counter += 1
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        x_pos = data.loc[data["states"] == f"{AnswerState}", "x"].values[0]
        y_pos = data.loc[data["states"] == f"{AnswerState}", "y"].values[0]
        t.goto(x_pos, y_pos)
        t.write(AnswerState, align="center", font=("Arial", 8, "normal"))

    # Exit the game
    if AnswerState.lower() == "exit":
        statesNotGuessed = [state for state in stateNames if state not in guessedStates]
        New_data = pandas.DataFrame(statesNotGuessed)
        New_data.to_csv("StatesToLearn.csv")
        break

    # Skip if input was empty
    if not AnswerState:
        continue
