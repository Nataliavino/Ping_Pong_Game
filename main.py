import time
from turtle import Screen
from ball import Ball
from platform import Platform
from score import Score

screen = Screen()
screen.setup(800, 600)
screen.bgpic('bg.png')
screen.title('Ping Pong Game')
screen.tracer(0)

r_platform = Platform(350, 0)
l_platform = Platform(-350, 0)
ball = Ball()
score = Score()

screen.listen()
screen.onkey(r_platform.up,'Up')
screen.onkey(r_platform.down,'Down')
screen.onkey(l_platform.up,'w')
screen.onkey(l_platform.down,'s')

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with r_platform
    if ball.xcor() > 320 and ball.distance(r_platform) < 50:
        ball.bounce_x()

    # Detect collision with l_platform
    if ball.xcor() < -320 and ball.distance(l_platform) < 50:
        ball.bounce_x()

    # Detect R platform misses
    if ball.xcor() > 380:
        ball.reset()
        score.l_add_score()

    # Detect L platform misses
    if ball.xcor() < -380:
        ball.reset()
        score.r_add_score()




screen.exitonclick()