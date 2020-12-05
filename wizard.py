import pygame


class Wizard:
    """A class to manage the wizard."""

    def __init__(self, ga_game):
        """Initialize the wizard and set its starting position."""

        self.screen = ga_game.screen
        self.settings = ga_game.settings
        self.screen_rect = ga_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/wizard.bmp')
        self.rect = self.image.get_rect()

        self.center_wizard()

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        # Update the ship's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.wizard_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.wizard_speed

        # Update rect object from self.x.
        self.rect.x = self.x

    def blitme(self):
        """Draw the wizard at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_wizard(self):
        """Center the wizard on the screen."""
        # Start each new wizard at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom
        # Store a decimal value for the wizard's horizontal position.
        self.x = float(self.rect.x)
