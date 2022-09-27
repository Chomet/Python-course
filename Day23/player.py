import turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.pu()
        self.reset()

    def move(self):
        self.setpos((self.xcor(), self.ycor() + MOVE_DISTANCE))

    def reset(self):
        self.setpos(STARTING_POSITION)
        self.setheading(90)
