import turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 10
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.carlist = []
        self.carspeed = STARTING_MOVE_DISTANCE
        self.spawn_cars()

    def spawn_cars(self):
        if random.randint(0, 10) > 6:
            newcar = turtle.Turtle()
            newcar.shape("square")
            newcar.color(random.choice(COLORS))
            newcar.shapesize(1, 2)
            newcar.pu()
            newcar.goto(350, random.randint(-250, 270))
            self.carlist.append(newcar)
            time.sleep(0.03)

    def car_move(self):
        for car in self.carlist:
            if car.xcor() > -350:
                car.goto((car.xcor() - self.carspeed, car.ycor()))
            else:
                self.carlist.remove(car)

    def reset(self):
        self.carspeed += MOVE_INCREMENT
