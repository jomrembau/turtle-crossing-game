from turtle import Turtle, Screen
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

lanes = [-125, -50, 25, 100, 175]

class Cars:

    def __init__(self):
        self.car_list = []
        self.screen = Screen()

    def move_cars(self):
        for car in self.car_list:
            car["turtle"].back(car["speed"])
            if car["turtle"].xcor() <= -260:
                car["turtle"].hideturtle()
                self.car_list.remove(car)

    def generate_cars(self):
        if len(self.car_list) <= 10:
            x = Turtle(visible=False)
            x.penup()
            x.shape("square")
            x.color(random.choice(colors))
            x.shapesize(stretch_len=3, stretch_wid=1)
            x.goto(250, random.choice(lanes))
            x.showturtle()
            self.car_list.append({"turtle": x, "speed": random.randint(5,20)})
            self.screen.ontimer(self.generate_cars,2000)




