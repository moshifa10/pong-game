from turtle import Turtle

# In this class I will create class for the first padel that will move left or right
# STARTING_POS = [(0,0),(0,20),(0,40)]
X_POS = 372
Y_POS = 0
INCREMENT = 20
class Padel2:

    def __init__(self):
        self.all_head = []
        self.create_player()


    def create_player(self):
        player = Turtle(shape="square")
        player.turtlesize(stretch_wid=5,stretch_len=1)
        player.color("white")
        player.penup()
        player.goto(x=X_POS, y=Y_POS)
        self.all_head.append(player)

    def up(self):
        for i in self.all_head:
            x, y = i.pos()
        self.all_head[0].goto(x,y+INCREMENT)

    def down(self):
        for i in self.all_head:
            x, y = i.pos()
        self.all_head[0].goto(x,y-INCREMENT)
