from turtle import Screen
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# It's good practice to have separate directories for different asset types.
# Let's assume your background image is in an 'images' folder inside 'assets'.
IMAGES_DIR = os.path.join(SCRIPT_DIR, 'assets', 'images')
BG_IMAGE = os.path.join(IMAGES_DIR, 'background_pic.gif') # Corrected typo and path

class Game:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=900, height=600)
        # Note: The turtle module's bgpic() method works most reliably with .gif files.
        # You might need to convert your .jpg to a .gif.
        self.screen.bgpic(BG_IMAGE)
        self.screen.title("My Snake Game")
        self.screen.tracer(0)
