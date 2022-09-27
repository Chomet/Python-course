import turtle
# Standard logo orientation is this one:
#           90
#            |
#       180 - - 0
#            |
#           270


class Scoreboard(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.scoreplayer1 = 0
        self.scoreplayer2 = 0
        self.color("white")
        self.pu()
        self.hideturtle()
        self.update_score(0)

    def update_score(self, xball):
        if xball > 0:
            self.scoreplayer1 += 1
        elif xball < 0:
            self.scoreplayer2 += 1
        self.clear()
        self.setpos(-40, 250)
        self.write(f"{self.scoreplayer1}", True, "center", ("Arial", 30, "normal"))
        self.setpos(40, 250)
        self.write(f"{self.scoreplayer2}", True, "center", ("Arial", 30, "normal"))
        self.setpos(0, 300)
        self.setheading(270)
        while self.ycor() > -300:
            self.pd()
            self.fd(10)
            self.pu()
            self.fd(10)

    def check_winner(self):
        if self.scoreplayer1 == 5:
            self.setpos(0, -20)
            self.write("Winner is player on the left!", True, "center", ("Arial", 20, "normal"))
            return True
        elif self.scoreplayer2 == 5:
            self.setpos(0, -20)
            self.write("Winner is player on the right!", True, "center", ("Arial", 20, "normal"))
            return True
        else:
            return False
