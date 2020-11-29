import pygame
import sys


class GhostsAttack:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 600))
        pygame.display.set_caption("Ghosts Attack")
        # Variables to synchronize refresh the game and FPS.
        self.FPS = 60
        self.clock = pygame.time.Clock()

    def run_game(self):
        """Start the main loop for the game."""

        while True:
            # Reduce game update to frames per second. Save PC resource
            self.clock.tick(self.FPS)
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Make the most recently drawn screen visible.
            pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game
    ga = GhostsAttack()
    ga.run_game()
