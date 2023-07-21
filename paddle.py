from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.shape("square")
        self.penup()
        self.goto(position)

    def go_up(self):
        if self.ycor() != 240:
            new_y_pos = self.ycor() + 20
            self.goto(self.xcor(), new_y_pos)

    def go_down(self):
        if self.ycor() != -240:
            new_y_pos = self.ycor() - 20
            self.goto(self.xcor(), new_y_pos)

    def goUp(self):
        if self.ycor() != 240:
            new_y_pos = self.ycor() + 20
            self.goto(self.xcor(), new_y_pos)

    def goDown(self):
        if self.ycor() != -240:
            new_y_pos = self.ycor() - 20
            self.goto(self.xcor(), new_y_pos)
