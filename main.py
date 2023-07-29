from turtle import Screen, Turtle
from scoreboard import Scoreboard
from paddle import Paddle
from time import sleep
from ball import Ball

# Screen setup
my_screen = Screen()
my_screen.setup(width=800, height=600)
my_screen.bgcolor('black')
my_screen.title('PongGame')
my_screen.tracer(0)

# Creating an instance of the Paddle class
left_paddle = Paddle((-390, 0))
right_paddle = Paddle((380, 0))

# Creating an intance of the ball class
ball = Ball()

# Creating an instance of the scoreboard class
scoreboard = Scoreboard()

# Activating the screen listen() function.
my_screen.listen()

# Listening for the right paddle key strokes
my_screen.onkey(right_paddle.go_up, 'Up')
my_screen.onkey(right_paddle.go_down, 'Down')

# Listening for the left paddle key strokes
my_screen.onkey(left_paddle.goUp, 'w')
my_screen.onkey(left_paddle.goDown, 's')

isGameOn = True
SLEEP_TIME = 0.1

while isGameOn:
    my_screen.update()
    sleep(SLEEP_TIME)
    ball.move_ball()

    # checking if the ball colides with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()

    # checking if the ball colides with the right paddle
    if ball.distance(right_paddle)< 50 and ball.xcor() > 350:
        ball.paddle_bounce()
        scoreboard.right_point()
        scoreboard.score_update()
           
    # checking if the ball collides with the left paddle
    if ball.distance(left_paddle) < 50 and ball.xcor() < -360:
        ball.paddle_bounce()
        scoreboard.left_point()
        scoreboard.score_update()     
             
    # checking if the paddle misses the ball
    if ball.xcor() > 400:
        ball.reset_ball()
        scoreboard.left_point()
        scoreboard.score_update()
        
    if ball.xcor() < -400:
        ball.reset_ball()
        scoreboard.right_point()
        scoreboard.score_update()
          
my_screen.exitonclick()
