from turtle import Turtle
import random

# --- FONT CONFIGURATION ---
# To use a custom font, you must first install it on your operating system.
# 1. Place your font file (e.g., 'PressStart2P-Regular.ttf') in an 'assets/fonts' directory.
# 2. Install the font on your system (e.g., right-click -> Install on Windows).
# 3. Find the exact "font name" and use it here.
# The name must match the one your OS uses. For example, for the file 'NewTegomin-Regular.ttf',
# the font name is typically 'New Tegomin'.
CUSTOM_FONT_NAME = "New TegoMiN"
ALIGNMENT = "center"
FONT = (CUSTOM_FONT_NAME, 20, "normal")  # Adjusted size for the new font
SCORE_FONT = (CUSTOM_FONT_NAME, 15, "bold")
GAME_OVER_FONT = (CUSTOM_FONT_NAME, 28, "bold") # Adjusted size for the new font
MESSAGE_FONT = (CUSTOM_FONT_NAME, 36, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.load_high_score()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()


    # In scoreboard.py, add these methods to the Scoreboard class:

    def update_scoreboard(self):
        self.clear()
        self.goto(350, 230)  # Place at the very top
        self.color("blue")  # Use a bold, eye-catching color
        self.write(
            f"Score: {self.score}\nHigh Score: {self.high_score}",
            align=ALIGNMENT,
            font=SCORE_FONT
        )

    def show_message(self, message, y=220):
        self.goto(0, y)
        self.color("black")
        self.write(message, align=ALIGNMENT, font=MESSAGE_FONT)

    def clear_message(self):
        self.clear()

    def game_over(self):
        # Update high score if the current score is higher
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=GAME_OVER_FONT)
        self.goto(0, -40)
        self.write("Press Space to Restart", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        """Resets the score for a new game and updates the display."""
        self.score = 0
        self.update_scoreboard()

    def show_pause_message(self):
        """Displays the PAUSED message on the screen."""
        self.goto(0, 0)
        self.write("PAUSED", align=ALIGNMENT, font=GAME_OVER_FONT)

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
