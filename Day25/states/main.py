from turtle import Turtle, Screen
import pandas

data = pandas.read_csv("50_states.csv")
dict = data.to_dict()

screen = Screen()
turtle = Turtle()
turtle.pu()
turtle.ht()
screen.setup(width=725, height=491)
screen.bgpic("blank_states_img.gif")
cont = True
high_score = 0
while cont:
    cont = False
    inp = screen.textinput(f"Current score: {high_score}/50", "Input the state!").title()
    for elem in dict["state"]:
        if dict["state"][elem] == inp:
            high_score += 1
            turtle.goto(dict["x"][elem], dict["y"][elem])
            turtle.write(dict["state"][elem])
            del dict["state"][elem]
            print("Yes")
            cont = True
            break

screen.exitonclick()
