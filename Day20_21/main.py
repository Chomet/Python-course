import turtle
import snake
import scoreboard
import food

window = turtle.Screen()
window.setup(600, 600)  # width, height
window.bgcolor("black")  # changing color of background
window.title("Snake game")  # name of screen
window.tracer(0)

scoreboard = scoreboard.Scoreboard()
food = food.Food()
snake = snake.Snake(scoreboard, food)

window.listen()
window.onkey(snake.up, "Up")
window.onkey(snake.down, "Down")
window.onkey(snake.left, "Left")
window.onkey(snake.right, "Right")

cont = True
while cont:
    cont = snake.move()

window.exitonclick()
