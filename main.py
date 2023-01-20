from scoreboard import Scoreboard
from time import sleep
from turtle import Screen
from stepper import Paddle
from ball import Ball

screen = Screen()
screen.title('First Game')
screen.bgcolor('black')
screen.setup(1250, 600)
screen.tracer(0)

r_paddle = Paddle((600, 0))
l_paddle = Paddle((-600, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
game_is_on = True
while game_is_on:
    sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detecting Collisions
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detecting contact with the paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Counting point of L player
    if ball.xcor() > 700:
        ball.reset_position()
        score.l_point()

    # Counting point of L player
    if ball.xcor() < -700:
        ball.reset_position()
        score.r_point()

screen.exitonclick()
