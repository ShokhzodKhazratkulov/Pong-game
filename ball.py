from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        x_coordinate = self.xcor() + self.x_move
        y_coordinate = self.ycor() + self.y_move
        self.goto(x_coordinate, y_coordinate)

    def bouncing_y(self):
        self.y_move *= -1

    def bouncing_x(self):
        self.x_move *= -1
        self.move_speed *= 0.8

    def reset_posit(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bouncing_x()

