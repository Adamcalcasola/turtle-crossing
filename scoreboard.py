from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.display()

    def display(self):
        self.clear()
        self.goto(-200, 250)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def level_up(self):
        self.level += 1
        self.display()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)