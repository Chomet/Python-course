import turtle


class Scoreboard(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore", "r") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.pu()
        self.hideturtle()
        self.setpos(0, 250)
        self.write(f"Score: {self.score} High Score: {self.high_score}", True, "center", ("Arial", 26, "normal"))

    def update_score(self):
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highscore", "w") as file:
                file.write(str(self.score))
        self.clear()
        self.setpos(0, 250)
        self.write(f"Score: {self.score} High Score: {self.high_score}", True, "center", ("Arial", 26, "normal"))

    def game_over(self):
        if self.score > self.high_score:
            self.high_score = self.score

