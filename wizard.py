import pygame


class Wizard:
    """A class to manage the wizard."""

    def __init__(self, ga_game):
        """Initialize the wizard and set its starting position."""

        self.screen = ga_game.screen
        self.screen_rect = ga_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/wizard.bmp')
        self.rect = self.image.get_rect()

        # Start each new wizard at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw the wizard at its current location."""
        self.screen.blit(self.image, self.rect)