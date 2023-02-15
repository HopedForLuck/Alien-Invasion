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

import sys

import pygame

from settings import Settings   # Module with settings for a game
from ship import Ship   # Module with a ship


def run_game():
    # Initializing game
    pygame.init()
    ai_settings = Settings()    # Creating instance ai_settings from class Settings from module settings.py

    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen)
    # Start the main loop for the game.
    while True:

        # Watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(ai_settings.bg_color)   # Redraw the screen during each pass through the loop.
        ship.blitme()

        pygame.display.flip()   # Make the most recently drawn screen visible.


run_game()
