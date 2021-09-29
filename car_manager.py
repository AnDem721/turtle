from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.cars = []
        self.car_positions = []
        self.starting_speed = STARTING_MOVE_DISTANCE
        
        
    def create_car(self):
            car_chance = random.randint(1,6)
            if car_chance == 6:
                car = Turtle('square')
                car.shapesize(1,2)
                car.color(random.choice(COLORS))
                car.penup()
                car.goto(300, random.randint(-250, 250))
                car.setheading(180)
                self.cars.append(car)
                       
    def move_car(self):
        for car in self.cars:
            car.forward(self.starting_speed)
            if car.xcor() < -350: 
                self.cars.remove(car)
         
    def level_up(self): 
        self.starting_speed += MOVE_INCREMENT
       

