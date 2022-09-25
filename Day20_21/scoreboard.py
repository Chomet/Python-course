import turtle


class Scoreboard(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.pu()
        self.hideturtle()
        self.setpos(0, 250)
        self.write(f"Score: {self.score}", True, "center", ("Arial", 26, "normal"))

    def update_score(self):
        self.score += 1
        self.clear()
        self.setpos(0, 250)
        self.write(f"Score: {self.score}", True, "center", ("Arial", 26, "normal"))
