from turtle import Turtle
# Here I will be creating the ball class

class Ball(Turtle):
    def __init__(self,width, height, color):
        super().__init__()
        self.shape("circle")
        self.color(color)
        self.penup()
        self.shapesize(stretch_len= width,stretch_wid=height)
        self.speed(0)

    
    def move(self):
        # get x_cor and y_core and increment both by 20
        x_cor, y_cor = self.position()
        self.goto(x_cor + 20, y_cor + 20)
        