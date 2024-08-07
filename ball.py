from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.01

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def wall_bounce(self):
        self.y_move *= -1
        #self.ball_speed *= 0.9 

    def paddle_bounce(self):
        self.ball_speed *= 0.9
        self.x_move *= -1

    def reset_ball(self):
        self.goto(0,0)
        self.ball_speed = 0.1
        self.paddle_bounce()

        

        
