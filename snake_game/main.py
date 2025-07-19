from snake import Snake
from food import Food
from scoreboard import Scoreboard
from game import Game
import pygame
import os
import time

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(SCRIPT_DIR, 'assets', 'sounds')
EAT_SOUND = os.path.join(ASSETS_DIR, 'eat.wav')
COLLISION_SOUND = os.path.join(ASSETS_DIR, 'collision.wav')
GAME_OVER_SOUND = os.path.join(ASSETS_DIR, 'game_over.wav')
BACKGROUND_MUSIC = os.path.join(ASSETS_DIR, 'background.wav')

# --- Game Constants ---
INITIAL_GAME_SPEED = 0.1
SPEED_INCREASE_THRESHOLD = 5
SPEED_MULTIPLIER = 0.9
MIN_SPEED = 0.04

pygame.mixer.pre_init(44100, -16, 2, 256)  # Add this line
pygame.init()
pygame.mixer.music.load(BACKGROUND_MUSIC)
pygame.mixer.music.set_volume(0.4)

eat_sound = pygame.mixer.Sound(EAT_SOUND)
collision_sound = pygame.mixer.Sound(COLLISION_SOUND)
game_over_sound = pygame.mixer.Sound(GAME_OVER_SOUND)

game = Game()
snake = Snake()
food = Food()
scoreboard = Scoreboard()

def show_countdown():
    """Displays a 'Ready, Steady, Go!' countdown in the center, hiding snake, food, and scoreboard."""
    # Hide snake, food, and scoreboard
    for segment in snake.segments:
        segment.hideturtle()
    food.hideturtle()
    scoreboard.clear()

    messages = ["Ready", "Steady", "Go!"]
    for msg in messages:
        scoreboard.show_message(msg, y=0)  # Center of the screen
        game.screen.update()
        time.sleep(0.8)
        scoreboard.clear_message()
        game.screen.update()
        time.sleep(0.2)

    # Show snake, food, and scoreboard after countdown
    for segment in snake.segments:
        segment.showturtle()
    food.showturtle()
    scoreboard.update_scoreboard()

# --- Game State ---
game_state = "playing"  # Can be "playing", "paused", "game_over"
game_speed = INITIAL_GAME_SPEED
food_eaten_counter = 0

# --- Game Functions ---
def toggle_pause():
    """Pauses or resumes the game."""
    global game_state
    if game_state == "playing":
        game_state = "paused"
        scoreboard.show_pause_message()
        pygame.mixer.music.pause()
    elif game_state == "paused":
        game_state = "playing"
        scoreboard.update_scoreboard()  # Clears the pause message
        pygame.mixer.music.unpause()

def restart_game():
    """Resets the game to its initial state after a game over."""
    global game_state, game_speed, food_eaten_counter
    if game_state == "game_over":
        game_state = "playing"
        scoreboard.reset()
        snake.reset()
        food.refresh()
        pygame.mixer.music.play(-1)
        game_speed = INITIAL_GAME_SPEED
        food_eaten_counter = 0

# --- Keybindings ---
game.screen.listen()
game.screen.onkey(snake.up, "w")
game.screen.onkey(snake.down, "s")
game.screen.onkey(snake.left, "a")
game.screen.onkey(snake.right, "d")
game.screen.onkey(toggle_pause, "p")
game.screen.onkey(restart_game, "space")

# --- Main Game Loop ---
pygame.mixer.music.play(-1)
# ...existing code...

show_countdown()

while True:
    if game_state == "playing":
        game.screen.update()
        time.sleep(game_speed) 
        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 20:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()
            eat_sound.play()

            # Increase difficulty
            food_eaten_counter += 1
            if food_eaten_counter % SPEED_INCREASE_THRESHOLD == 0:
                game_speed = max(MIN_SPEED, game_speed * SPEED_MULTIPLIER)

        # Detect collision with wall
        wall_collision = (
            snake.head.xcor() >  430 or snake.head.xcor() < -430 or
            snake.head.ycor() > 230 or snake.head.ycor() < -280
        )


        # Detect collision with tail
        tail_collision = False
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                tail_collision = True
                break

        # Handle collisions
        if wall_collision or tail_collision:
            pygame.mixer.music.stop()
            game_state = "game_over"
            scoreboard.game_over()
            if wall_collision:
                collision_sound.play()
            else:
                game_over_sound.play()
    else:
        # In "paused" or "game_over" state, keep the screen updated
        # to be responsive to key presses (like un-pausing or restarting).
        game.screen.update()
