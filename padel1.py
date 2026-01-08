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
        self.x_move = 10
        self.y_move = 10

    
    def move(self):
        # get x_cor and y_core and increment both by 20
        x_cor, y_cor = self.position()
        self.goto(x_cor + self.x_move, y_cor + self.y_move)

    def bounce_x(self):
        self.x_move *= -1

    def bounce_y(self):
        self.y_move *= -1

    def reset(self):
        self.goto(0,0)
        self.bounce_x()