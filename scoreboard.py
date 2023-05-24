from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 16, 'bold')
FONT1 = ('Courier', 8, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        with open("data.txt") as f:
            self.high_score = int(f.read())
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 275)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} The highest score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def check_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode='w') as f:
                f.write(str(self.high_score))

    def reset(self):
        self.score = 0
        self.goto(0, 275)
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def write_game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
