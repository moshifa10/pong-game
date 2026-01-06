from turtle import Turtle
from padel1 import Padel1
# In this class I will create class for the first padel that will move left or right
# STARTING_POS = [(0,0),(0,20),(0,40)]


INCREMENT = 20

class Padel2(Padel1):

    def __init__(self, x_coordinate, y_coordinate):
        super().__init__(x_coordinate,y_coordinate)
        self.all_head[0].goto(x_coordinate,y_coordinate)
