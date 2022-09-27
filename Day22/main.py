import turtle
import paddles
import scoreboard
import ball
import time

LEFT_START = (-385, 0)
RIGHT_START = (380, 0)

window = turtle.Screen()
window.setup(800, 600)  # width, height
window.bgcolor("black")  # changing color of background
window.title("Ping-pong")  # name of screen
window.tracer(0)

scoreboard = scoreboard.Scoreboard()
left_paddle = paddles.Paddle(LEFT_START)
right_paddle = paddles.Paddle(RIGHT_START)
ball = ball.Ball()
window.update()
window.listen()

window.onkeypress(left_paddle.up, "w")
window.onkeypress(left_paddle.down, "s")
window.onkeypress(right_paddle.up, "Up")
window.onkeypress(right_paddle.down, "Down")

speed_delay = 0.05
has_winner = False
while not has_winner:
    window.update()
    ball.move()
    xball = ball.ball.xcor()
    yball = ball.ball.ycor()
    if xball < -395 or xball > 395:
        scoreboard.update_score(xball)
        ball.reset()
        left_paddle.reset(LEFT_START)
        right_paddle.reset(RIGHT_START)
        window.update()
        has_winner = scoreboard.check_winner()
        time.sleep(2)
        speed_delay = 0.05
    elif yball < -290 or yball > 290:
        ball.collision_with_wall()
    elif ball.ball.distance(left_paddle.paddle) < 15:
        ball.collision_with_paddle()
        speed_delay *= 0.9
    elif ball.ball.distance(right_paddle.paddle) < 15:
        ball.collision_with_paddle()
        speed_delay *= 0.9
    time.sleep(speed_delay)

window.exitonclick()
