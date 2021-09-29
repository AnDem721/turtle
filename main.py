import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
screen.onkey(player.move_turle, 'Up')
game_is_on = True
car = CarManager()
score = Scoreboard()

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_car()
    for x in car.cars: 
        if player.distance(x) < 20: 
            game_is_on = False
            score.game_over()
    if player.ycor() > 270: 
        player.move_to_start()
        car.level_up()
        score.update_score()
    
        
       
        
    
    
screen.exitonclick()
