import turtle
import pandas as pd

ALIGN = "left"
FONT = ("Arial", 8, "normal")

data = pd.read_csv("50_states.csv")
#print(data)

screen = turtle.Screen()
screen.title("U.S. States Game")

img = "blank_states_img.gif"
screen.addshape(img)

turtle.shape(img)

answer_turtle = turtle.Turtle()
answer_turtle.hideturtle()
guessed_states = []

score = 0
while score < 50:
	answer_state = screen.textinput(title=f"{score}/50 Guess the state", prompt="What's another state's name?")
	if answer_state.title() == "Exit":
		missing_states = [x for x in data.state if x not in guessed_states]
		df = pd.DataFrame(missing_states)
		df.to_csv("states_to_learn.csv")
		break
	answer_turtle.penup()
	if len(data[data.state == answer_state.title()]) > 0:
		guessed_states.append(answer_state.title())
		score += 1
		current_answer = data[data.state == answer_state.title()]
		coords = (int(current_answer.x), int(current_answer.y))
		answer_turtle.goto(coords)
		answer_turtle.write(current_answer.state.item(), align=ALIGN, font=FONT)

if score >= 50:
	screen.textinput(title="You Won!", prompt="You Won! Press OK to Quit")
		


screen.exitonclick()