import turtle
import random
# import turtle as t
logo = turtle.Turtle()
# this is kinda weird, we need to create Screen object and change colormode there
# it affects whole turtle class
logo2 = turtle.Screen()
logo2.colormode(255)
# logo = t.Turtle()


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return logo.color((r, g, b))


logo.fd(100)
logo.lt(90)
logo.fd(100)
logo.lt(90)
logo.fd(100)
logo.lt(90)
logo.fd(100)
logo.rt(90)
for n in range(8):
    logo.fd(10)
    logo.pu()
    logo.fd(2)
    logo.pd()
for n in range(3, 11):
    random_color()
    for m in range(n):
        logo.fd(50)
        logo.lt(360/n)
logo.clear()
angles =[0, 90, 180, 270]
logo.speed("fastest")
for _ in range(300):
    random_color()
    logo.fd(20)
    logo.lt(random.choice(angles))
logo.reset()
for _ in range(40):
    random_color()
    logo.circle(100)
    logo.lt(360/40)



window = turtle.Screen()
window.exitonclick()