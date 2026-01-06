import turtle as t
from padel1 import Padel1
from padel2 import Padel2

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

padel1 = Padel1()
padel2 = Padel2()

# Make the screen listen to moves
screen.listen()
screen.onkey(fun=padel1.down, key="s")
screen.onkey(fun=padel1.up, key="w")
screen.onkey(fun=padel2.down, key="Down")
screen.onkey(fun=padel2.up, key="Up")


game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()