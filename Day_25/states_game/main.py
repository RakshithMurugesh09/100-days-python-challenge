import turtle
import pandas

IMAGE = "blank_india_img.gif"

data = pandas.read_csv("india_states.csv")
all_states = data.state.tolist()
guessed_states = []

screen = turtle.Screen()
screen.title("States Game")
screen.addshape(IMAGE)
turtle.shape(IMAGE)

while len(guessed_states) < len(all_states):
    user_answer = screen.textinput(f"{len(guessed_states)} / {len(all_states)} states left",
                     "Guess the next state").title().strip()
    if user_answer is None:
        break

    if user_answer == "Exit":
        print("Thanks for playing!")
        need_to_learn = [state for state in all_states if state not in guessed_states]
        print("You needed to still learn below states\n", need_to_learn)
        break

    if user_answer in all_states and user_answer not in guessed_states:
        guessed_states.append(user_answer)
        current_state = data[data.state == user_answer]

        x = current_state.x.item()
        y = current_state.y.item()

        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(x, y)
        t.write(user_answer)


screen.exitonclick()
