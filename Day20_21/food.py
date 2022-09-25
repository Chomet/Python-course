import turtle
import random


class Food(turtle.Turtle):

    def __init__(self):
        # Initial food properties (create it later in generate_food)
        super().__init__()
        self.color("yellow")
        self.shape("square")
        self.foodpos = None
        self.pu()
        self.generate_dot()

    def generate_dot(self):
        # We will just move food around so this function can be used when food is eaten too
        available_position = []
        x = -280
        y = -280
        while x <= 280:
            while y <= 280:
                available_position.append((x, y))
                y += 20
            y = -280
            x += 20
        position = random.choice(available_position)
        self.setpos(position)
        self.foodpos = position
        return position
