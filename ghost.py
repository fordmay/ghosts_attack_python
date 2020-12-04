import pygame
import random
from pygame.sprite import Sprite


class Ghost(Sprite):
    """A class to manage a single ghost in the crowd."""

    def __init__(self, ga_game):
        """Initialize the ghost and set its starting position."""
        super().__init__()
        self.screen = ga_game.screen
        self.settings = ga_game.settings

        # take random ghost image
        ghosts_list = ['ghost_blue', 'ghost_pink',
                       'ghost_yellow', 'ghost_green']
        take_image_ghost = f"images/{random.choice(ghosts_list)}.bmp"
        # Load the ghost image and set its rect attribute.
        self.image = pygame.image.load(take_image_ghost)
        self.rect = self.image.get_rect()

        # Start each new ghost near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the ghost's exact horizontal position.
        self.x = float(self.rect.x)

    def update(self):
        """Move the ghost right or left."""
        self.x += (self.settings.ghost_speed *
                   self.settings.crowd_direction)
        self.rect.x = self.x

    def check_edges(self):
        """Return True if ghost is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
