from turtle import Turtle

# In this class I will create class for the first padel that will move left or right

# STARTING_POS = [(0,0),(0,20),(0,40)]

INCREMENT = 20
class Padel1:

    def __init__(self, x_coordinate ,y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.all_head = []
        self.create_player(x_pos=x_coordinate, y_pos=y_coordinate)


    def create_player(self, x_pos, y_pos):
        player = Turtle(shape="square")
        player.turtlesize(stretch_wid=5,stretch_len=1)
        player.color("white")
        player.penup()
        player.goto(x=x_pos, y=y_pos)
        self.all_head.append(player)

    def up(self):
        for i in self.all_head:
            x, y = i.pos()
        self.all_head[0].goto(x,y+INCREMENT)

    def down(self):
        for i in self.all_head:
            x, y = i.pos()
        self.all_head[0].goto(x,y-INCREMENT)



# STARTING_POS = [(-380,0),(-380,20),(-380,40)]

# class Padel1:

#     def __init__(self):
#         self.all_head = []
#         self.create_player()


#     def create_player(self):
#         for x, y in STARTING_POS:
#             player = Turtle(shape="square")
#             player.color("white")
#             player.speed("fastest")
#             player.penup()
#             player.goto(x=x,y=y)
#             self.all_head.append(player)

#     # Here I will do function to move the head

#     def down(self):
#         for pos in range(len(self.all_head)-1, 0, -1):
#             self.all_head[pos].goto(self.all_head[pos-1].pos())
#         x,y = self.all_head[0].pos()
#         self.all_head[0].goto(x, y-20)

#     def up(self):
#         for pos in range(len(self.all_head)-1):
#             self.all_head[pos].goto(self.all_head[pos+1].pos())
#         print(self.all_head[-1].pos())
#         x,y = self.all_head[-1].pos()
#         self.all_head[-1].goto(x, y+20)

