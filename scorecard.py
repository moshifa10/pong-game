from turtle import Turtle

class ScoreCard(Turtle):
    def __init__(self, x_cor, y_cor, color):
        super().__init__()
        self.score = 0
        self.color(color)
        self.hideturtle()
        self.penup()
        self.goto(x_cor, y_cor)
        self.write_score()
        
    def increment_score(self):
        self.score += 1
        self.clear()

    def write_score(self):
        self.write(
            arg= f"{self.score}",
            move=False,
            align="center",
            font= ("Arial",50 , "normal")
        )