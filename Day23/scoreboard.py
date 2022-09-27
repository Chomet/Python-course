import turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.level = 0
        self.color("black")
        self.pu()
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.level += 1
        self.setpos(-220, 260)
        self.write(f"Level: {self.level}", True, "center", FONT)

    def end_screen(self):
        self.setpos(0, 0)
        self.write("Game over!", True, "center", FONT)

