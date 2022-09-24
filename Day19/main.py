import turtle

logo = turtle.Turtle()
window = turtle.Screen()
window.colormode(255)


def move_forwards():
    logo.fd(10)


def move_backwards():
    logo.bk(10)


def go_left():
    logo.lt(5)


def go_right():
    logo.rt(5)


def clear_screen():
    logo.reset()


window.listen()
# onkey is higher order function since it uses other function as parameter
window.onkey(move_forwards, "w")
window.onkey(move_backwards, "s")
window.onkey(go_left, "a")
window.onkey(go_right, "d")
window.onkey(clear_screen, "c")
window.exitonclick()
