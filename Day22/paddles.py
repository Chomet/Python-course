import turtle


class Paddle:

    def __init__(self, position):
        # Keeping snake parts, positions and last position
        self.paddleparts = []
        # Creating paddle
        self.paddle = turtle.Turtle("square")
        self.paddle.color("white")
        self.paddle.pu()
        self.paddle.shapesize(3, 1)
        self.paddle.setpos(position)

    def up(self):
        if self.paddle.ycor() < 280:
            self.paddle.setposition((self.paddle.xcor(), self.paddle.ycor() + 20))

    def down(self):
        if self.paddle.ycor() > -280:
            self.paddle.setposition((self.paddle.xcor(), self.paddle.ycor() - 20))

    def reset(self, position):
        self.paddle.setpos(position)
