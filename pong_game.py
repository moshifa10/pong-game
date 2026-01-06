import turtle as t
from padel1 import Padel1
from padel2 import Padel2
from ball import Ball
import time

'''
    I will be creating a pong game using turtle

    How will I structure the Game into small peaces
        1. Create the screen
        2. Create and move a paddle
        3. Create another paddle
        4. Create the ball and make it move
        5. Detect collision with wall and bounce
        6. Detect collision with paddle
        7. Detect when paddle misses
        8. Keep score

'''


# Screen
screen = t.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

# right Padel starting position 
X_POS = -380
Y_POS = 0
padel1_r = Padel1(X_POS, Y_POS)

# Left Padel starting position
X_POS_padel_left = 372
Y_POS_padel_left = 0
padel2_l = Padel2(X_POS_padel_left, Y_POS_padel_left)

# Ball Functionality
ball = Ball(1,1, "red")

# Make the screen listen to moves
screen.listen()
screen.onkey(fun=padel1_r.down, key="s")
screen.onkey(fun=padel1_r.up, key="w")
screen.onkey(fun=padel2_l.down, key="Down")
screen.onkey(fun=padel2_l.up, key="Up")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    ball.move()
    

screen.exitonclick()