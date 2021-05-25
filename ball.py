from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")

    def move(self):
        for _ in range(50):
            new_x = self.xcor() + 1
            new_y = self.ycor() + 1
            self.penup()
            self.goto(new_x, new_y)