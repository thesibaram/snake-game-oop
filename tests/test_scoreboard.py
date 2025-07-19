from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 18, "bold")
GAME_OVER_FONT = ("Arial", 24, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.load_high_score()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        # Update high score if the current score is higher
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
        self.goto(0,0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=GAME_OVER_FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def load_high_score(self):
        try:
            with open("data.txt", "r") as f:
                self.high_score = int(f.read())
        except (FileNotFoundError, ValueError):
            # If file doesn't exist or is empty/corrupt, start high score at 0
            self.high_score = 0

    def save_high_score(self):
        with open("data.txt", "w") as f:
            f.write(str(self.high_score))
