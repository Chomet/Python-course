import turtle
import random

window = turtle.Screen()
window.colormode(255)
window.setup(500, 400)  # width, height
bet = int(window.textinput("Turtle race", "Which turtle will win (numbers are 1-6)"))

turtles = []
for n in range(6):
    logo = turtle.Turtle("turtle")
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    logo.color((r, g, b))
    logo.pu()
    logo.setpos(-230, 30 * n)
    turtles.insert(0, logo)

cont = True
victorious = -1
while cont:
    for turtle in turtles:
        turtle.fd(random.randint(1, 8))
        (x, y) = turtle.pos()
        if x > 250:
            print("We have a victorious turtle!")
            cont = False
            victorious = turtles.index(turtle)
            break

if bet == victorious + 1:
    print("Your turtle won!")
else:
    print(f"Your turtle lost! Turtle number {victorious + 1} won")

window.exitonclick()
