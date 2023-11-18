from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 80, 'normal')

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('#1a2ce1')
        self.l_score = 0
        self.r_score = 0
        self.show_score()

    def l_add_score (self):
        self.clear()
        self.l_score += 1
        self.show_score()

    def r_add_score (self):
        self.clear()
        self.r_score += 1
        self.show_score()


    def show_score(self):
        self.goto(-100, 200)
        self.write(self.l_score, False, ALIGNMENT, FONT)
        self.goto(100, 200)
        self.write(self.r_score, False, ALIGNMENT, FONT)