from turtle import Turtle

FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.num = 1
        self.hideturtle()

    def level(self):
        self.penup()
        self.hideturtle()
        self.goto(-230, 260)
        self.write(f"Level: {self.num}", align="Center", font=FONT)

    def game_over(self):
        self.write("Game Over", align="Center", font=FONT)

    def level_up(self):
        self.num += 1
        self.clear()
        self.write(f"Level: {self.num}", align="Center", font=FONT)
