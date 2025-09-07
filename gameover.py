from turtle import Turtle

class GameOver:

    def __init__(self):
        self.text = Turtle(visible=False)
        self.text.color("black")

    def end_game(self):
        self.text.showturtle()
        self.text.write("G A M E  O V E R", font=("Arial", 24, " "), align = "center")
