import turtle
import random

DIRECTIONS = ["leftup", "leftdown", "rightup", "rightdown"]


class Ball:

    def __init__(self):
        # Initial food properties (create it later in generate_food)
        self.ball = turtle.Turtle("square")
        self.ball.color("yellow")
        self.ball.shape("square")
        self.ball.pu()
        self.current_direction = random.choice(DIRECTIONS)

    def move(self):
        x = self.ball.xcor()
        y = self.ball.ycor()
        if self.current_direction == "leftup":
            self.ball.setposition((x - 8, y + 8))
        if self.current_direction == "leftdown":
            self.ball.setposition((x - 8, y - 8))
        if self.current_direction == "rightup":
            self.ball.setposition((x + 8, y + 8))
        if self.current_direction == "rightdown":
            self.ball.setposition((x + 8, y - 8))

    def collision_with_wall(self):
        x = self.ball.xcor()
        y = self.ball.ycor()
        if self.current_direction == "leftup":
            self.current_direction = "leftdown"
            self.ball.setposition((x - 8, y - 8))
        elif self.current_direction == "leftdown":
            self.current_direction = "leftup"
            self.ball.setposition((x - 8, y + 8))
        elif self.current_direction == "rightup":
            self.current_direction = "rightdown"
            self.ball.setposition((x + 8, y - 8))
        elif self.current_direction == "rightdown":
            self.current_direction = "rightup"
            self.ball.setposition((x + 8, y + 8))

    def collision_with_paddle(self):
        x = self.ball.xcor()
        y = self.ball.ycor()
        if self.current_direction == "leftup":
            self.current_direction = "rightup"
            self.ball.setposition((x + 8, y + 8))
        elif self.current_direction == "leftdown":
            self.current_direction = "rightdown"
            self.ball.setposition((x + 8, y - 8))
        elif self.current_direction == "rightup":
            self.current_direction = "leftup"
            self.ball.setposition((x - 8, y - 8))
        elif self.current_direction == "rightdown":
            self.current_direction = "leftdown"
            self.ball.setposition((x - 8, y + 8))

    def reset(self):
        self.ball.setposition(0, 0)
        self.current_direction = random.choice(DIRECTIONS)
