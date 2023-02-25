"""
In Alien Invasion, the player controls a ship that appears at
the bottom center of the screen. The player can move the ship
right and left using the arrow keys and shoot bullets using the
spacebar. When the game begins, a fleet of aliens fills the sky
and moves across and down the screen. The player shoots and
destroys the aliens. If the player shoots all the aliens, a new fleet
appears that moves faster than the previous fleet. If any alien hits
the player’s ship or reaches the bottom of the screen, the player
loses a ship. If the player loses three ships, the game ends.
contributions:
ship - <a href="https://www.freepik.com/free-vector/rocket-sky_4923760.htm#query=starship&position=2&from_view=search&track=sph">Image by brgfx</a> on Freepik

"""

import pygame
from pygame.sprite import Group

from settings import Settings   # Module with settings for a game
from ship import Ship   # Module with a ship
import game_functions as gf


def run_game():
    # Initializing game
    pygame.init()
    ai_settings = Settings()    # Creating instance ai_settings from class Settings from module settings.py

    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(ai_settings, screen)

    bullets = Group()   # Group that stores bullets
    aliens = Group()  # Group that stores aliens

    gf.create_fleet(ai_settings, screen, aliens)

    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)   # Check for keyboard or mouse events
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)    # Updating screen with every loop


run_game()
