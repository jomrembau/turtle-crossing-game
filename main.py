from turtle import Screen
from player import Player
from cars import Cars
from score import Score
from gameover import GameOver

win = Screen()

final_screen = GameOver()
t_player = Player()
vehicle = Cars()
game_score = Score()
difficulty = 100

win.setup(500,500)
win.title("Turtle Crossing Game")
win.tracer(0)

win.listen()
win.onkey(t_player.move_up, "Up")

def game_on():
    win.update()
    vehicle.move_cars()

    if t_player.michael.ycor() >= 200:
        game_score.current_level += 1
        t_player.reset_turtle()
        game_score.update_score()

    win.ontimer(game_on, difficulty)

game_on()

win.exitonclick()