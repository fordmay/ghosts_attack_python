import pygame
from random import randint
from pygame.sprite import Sprite


class Ball(Sprite):
    """A class to manage ball fired from the wizard"""

    def __init__(self, ga_game):
        """Create a ball object at the wizard's current position."""
        super().__init__()
        self.screen = ga_game.screen
        self.settings = ga_game.settings
        # Take random color to ball
        self.color = (randint(0, 255), randint(0, 255), randint(0, 255))

        # Create a ball rect at (0, 0) and then set correct position
        self.rect = pygame.Rect(0, 0, self.settings.ball_width,
                                self.settings.ball_height)
        self.rect.midtop = ga_game.wizard.rect.midtop

        # Store the ball's position as a decimal value.
        self.y = float(self.rect.y)

    def update(self):
        """Move the ball up the screen."""
        # Update the decimal position of the bullet
        self.y -= self.settings.ball_speed
        # Update the rect position.
        self.rect.y = self.y

    def draw_ball(self):
        """Draw the ball to the screen."""
        pygame.draw.ellipse(self.screen, self.color, self.rect)
