import pygame
import sys
from settings import Settings
from wizard import Wizard
from ball import Ball


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

        self.wizard = Wizard(self)
        self.balls = pygame.sprite.Group()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.wizard.update()
            self.balls.update()
            self._update_screen()

    def _check_events(self):
        """Respond to key presses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to key presses."""
        if event.key == pygame.K_RIGHT:
            self.wizard.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.wizard.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_ball()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.wizard.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.wizard.moving_left = False

    def _fire_ball(self):
        """Create a new ball and add it to the balls group."""
        new_ball = Ball(self)
        self.balls.add(new_ball)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Reduce redraw the screen to FPS. Save PC resource
        self.clock.tick(self.settings.FPS)
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        # Add the wizard to the game
        self.wizard.blitme()
        # Add the balls to the game
        for ball in self.balls.sprites():
            ball.draw_ball()
        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game
    ga = GhostsAttack()
    ga.run_game()
