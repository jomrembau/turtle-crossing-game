from turtle import Turtle

class Score:
    def __init__(self):
        self.difficulty = 100
        self.level = Turtle(visible = False)
        self.level.penup()
        self.level.goto(-220,210)
        self.current_level = 0
        self.level.color("blue")
        self.level.write(f"Score: {self.current_level}", font=("Arial", 16, " "), align = "left")

    def update_score(self):
        self.level.clear()
        self.level.write(f"Score: {self.current_level}", font=("Arial", 16, " "), align="left")
        self.difficulty -= 4
