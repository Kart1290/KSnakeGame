from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 12, 'normal')
GAME_OVER_FONT = ('Courier', 24, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        with open("data.txt", mode='r') as file:
            self.high_score = int(file.read())
        self.ht()
        self.penup()
        self.goto(0, 280)
        self.score_counter()

    def score_counter(self):
        self.pencolor('white')
        self.score += 1
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.high_score}', move=False, align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write('GAME OVER!', move=False, align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            with open('data.txt', mode='w') as file:
                file.write(str(self.score))
            self.high_score = self.score
        self.score = -1
        self.score_counter()
