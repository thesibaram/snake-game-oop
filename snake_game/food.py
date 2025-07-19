from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1) # Make it half the default size
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x = random.randint(-420, 350)
        y = random.randint(-260, 230)
        self.goto(x, y)
