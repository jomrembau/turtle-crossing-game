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

def game_on():
    win.update()

    vehicle.generate_cars()
    vehicle.move_cars()

    if t_player.michael.ycor() >= 250:
        game_score.current_level += 1
        t_player.reset_turtle()
        game_score.update_score()

    for car in vehicle.car_list:
        if t_player.michael.distance(car["turtle"]) < 30:
            final_screen.end_game()
            return

    win.ontimer(game_on, game_score.difficulty)

win.setup(500,500)
win.title("Turtle Crossing Game")
win.tracer(0)

win.listen()
win.onkey(t_player.move_up, "Up")

game_on()


win.exitonclick()
