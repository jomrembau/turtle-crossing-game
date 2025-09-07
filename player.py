from turtle import Turtle

class Player:
    def __init__(self):
        self.michael = Turtle(visible=False)
        self.michael.shape("turtle")
        self.michael.penup()
        self.michael.setheading(90)
        self.michael.goto(0,-220)
        self.michael.showturtle()

    def move_up(self):
        self.michael.forward(15)

    def reset_turtle(self):
        self.michael.hideturtle()
        self.michael.goto(0,-220)
        self.michael.showturtle()

