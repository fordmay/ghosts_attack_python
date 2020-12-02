import pygame
from pygame.sprite import Sprite


class Ghost(Sprite):
    """A class to manage a single ghost in the crowd."""

    def __init__(self, ga_game):
        """Initialize the ghost and set its starting position."""
        super().__init__()
        self.screen = ga_game.screen

        # Load the ghost image and set its rect attribute.
        self.image = pygame.image.load('images/ghost.bmp')
        self.rect = self.image.get_rect()

        # Start each new ghost near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the ghost's exact horizontal position.
        self.x = float(self.rect.x)

