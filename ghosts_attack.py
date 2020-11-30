import pygame
import sys
from settings import Settings
from wizard import Wizard


class GhostsAttack:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Ghosts Attack")

        # Variable for control time.
        self.clock = pygame.time.Clock()

        # Create object a wizard
        self.wizard = Wizard(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """Respond to key presses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Reduce redraw the screen to FPS. Save PC resource
        self.clock.tick(self.settings.FPS)
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        # Add the wizard to the game
        self.wizard.blitme()
        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game
    ga = GhostsAttack()
    ga.run_game()
