from turtle import Turtle
import random

colors = [
    "red",
    "blue",
    "green",
    "yellow",
    "orange",
    "purple",
    "pink",
    "brown",
    "black",
    "gray",
    "cyan",
    "magenta"
]

lanes = [-150, -100, -50, 0, 50, 100, 150 ]

class Cars:

    def __init__(self):
        self.auto = Turtle(visible=False)
        self.auto.shape("square")
        self.auto.color(random.choice(colors))
        self.auto.shapesize(stretch_wid=1, stretch_len=3)
        self.auto.penup()
        self.random_movement = random.randint(5,15)
        self.auto.goto(250,random.choice(lanes))
        self.auto.showturtle()

    def move_cars(self):
        self.auto.back(self.random_movement)
