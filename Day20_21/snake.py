import turtle
import time
import copy


class Snake:

    def __init__(self, scoreboard, food):
        # Keeping snake parts, positions and last position
        self.snakepositions = [(0, 0), (-20, 0), (-40, 0)]
        self.snakeparts = []
        self.lastpos = (-40, 0)
        # Window object, only used to update current situation
        self.window = turtle.Screen()
        self.current_direction = "Right"
        # Food and scores turtles
        self.food = food
        self.scores = scoreboard
        # Creating initial snake and saving parts in list
        for position in self.snakepositions:
            bodypart = turtle.Turtle("square")
            bodypart.color("white")
            bodypart.pu()
            bodypart.setpos(position)
            self.snakeparts.append(bodypart)
        self.window.update()
        # Generate food on screen
        self.generate_dot()

    # Snake can't do 180 in one move
    def up(self):
        if self.current_direction != "Down":
            self.current_direction = "Up"

    def down(self):
        if self.current_direction != "Up":
            self.current_direction = "Down"

    def left(self):
        if self.current_direction != "Right":
            self.current_direction = "Left"

    def right(self):
        if self.current_direction != "Left":
            self.current_direction = "Right"

    def generate_dot(self):
        # Generate food until it's not positioned on spae occupied by snake
        already_occupied = True
        while already_occupied:
            possible_position = self.food.generate_dot()
            if possible_position not in self.snakepositions:
                already_occupied = False

    def grow_snake(self):
        # Generate new bodypart at the place of where tail was before head eat the food
        bodypart = turtle.Turtle("square")
        bodypart.color("white")
        bodypart.pu()
        bodypart.setpos(self.lastpos)
        self.snakepositions.append(self.lastpos)
        # Update the bodyparts list
        self.snakeparts.append(bodypart)
        # Generate new food and update total score
        self.generate_dot()
        self.scores.update_score()

    def move(self):
        n = 0
        # 0.15 seconds is pretty smooth, you can still do weird movements with rapid pressing of keys thou
        time.sleep(0.15)
        (x, y) = self.snakepositions[0]
        # Make a deep copy of original positions
        oldpositions = copy.deepcopy(self.snakepositions)
        # Update last position, needed if snake will grow after moving
        self.lastpos = self.snakepositions[len(self.snakepositions) - 1]
        # Head position needs to be adjusted by 20 pixels in whichever direction snake was heading
        # Also check if head made a collision with body
        if self.current_direction == "Up":
            self.snakeparts[0].setpos(x, y + 20)
            if (x, y + 20) not in self.snakepositions:
                self.snakepositions[0] = (x, y + 20)
            else:
                return False
        elif self.current_direction == "Right":
            self.snakeparts[0].setpos(x + 20, y)
            if (x + 20, y) not in self.snakepositions:
                self.snakepositions[0] = (x + 20, y)
            else:
                return False
        elif self.current_direction == "Down":
            self.snakeparts[0].setpos(x, y - 20)
            if (x, y - 20) not in self.snakepositions:
                self.snakepositions[0] = (x, y - 20)
            else:
                return False
        elif self.current_direction == "Left":
            self.snakeparts[0].setpos(x - 20, y)
            if (x - 20, y) not in self.snakepositions:
                self.snakepositions[0] = (x - 20, y)
            else:
                return False
        # Body positions will just be last position of body part which is in front of them
        for bodypart in self.snakeparts:
            if n > 0:
                bodypart.setpos(oldpositions[n - 1])
                self.snakepositions[n] = (oldpositions[n - 1])
            n += 1
        self.window.update()
        (x, y) = self.snakepositions[0]
        # Check if head is at food position
        if self.food.foodpos == (x, y):
            self.grow_snake()
        # Check if head made a collision with edges of screen
        if x <= -300 or x >= 300 or y <= -300 or y >= 300:
            return False
        else:
            return True
