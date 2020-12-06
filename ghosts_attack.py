import sys
from time import sleep
import pygame
from settings import Settings
from wizard import Wizard
from ball import Ball
from ghost import Ghost
from game_stats import GameStats
from button import Button


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

        # Create an instance to store game statistics
        self.stats = GameStats(self)

        self.wizard = Wizard(self)
        self.balls = pygame.sprite.Group()
        self.ghosts = pygame.sprite.Group()
        self._create_crowd()

        # Make the Play button.
        self.play_button = Button(self, "Play")

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Reduce redraw the screen to FPS. Save PC resource
            self.clock.tick(self.settings.FPS)

            self._check_events()
            if self.stats.game_active:
                self.wizard.update()
                self._update_balls()
                self._update_ghosts()

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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

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
        if len(self.balls) < self.settings.balls_allowed:
            new_ball = Ball(self)
            self.balls.add(new_ball)

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # Reset the game statistics.
            self.stats.reset_stats()
            self.stats.game_active = True
            # Get rid of any remaining ghosts and balls.
            self.ghosts.empty()
            self.balls.empty()
            # Create a new crowd and center the wizard.
            self._create_crowd()
            self.wizard.center_wizard()
            # Hide the mouse cursor.
            pygame.mouse.set_visible(False)

    def _update_balls(self):
        """Update position of balls and get rid of old balls."""
        # Update balls positions
        self.balls.update()

        # Get rid of balls that have disappeared.
        for ball in self.balls.copy():
            if ball.rect.bottom <= 0:
                self.balls.remove(ball)

        self._check_ball_ghost_collisions()

    def _check_ball_ghost_collisions(self):
        """Respond to ball-ghost collisions."""
        # Remove any ballets and ghosts that have collided.
        pygame.sprite.groupcollide(self.balls, self.ghosts, True, True)

        if not self.ghosts:
            # Destroy existing balls and create new crowd.
            self.balls.empty()
            self._create_crowd()

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        # Add the wizard to the game
        self.wizard.blitme()
        # Add balls to the game
        for ball in self.balls.sprites():
            ball.draw_ball()
        # Add ghosts to the game
        self.ghosts.draw(self.screen)
        # Draw the play button if the game is inactive.
        if not self.stats.game_active:
            self.play_button.draw_button()
        # Make the most recently drawn screen visible.
        pygame.display.flip()

    def _create_crowd(self):
        """Create the crowd of ghosts."""
        # Create a ghost and find the number of ghosts in a row.
        # Spacing between each ghost is equal to one ghost width.
        ghost = Ghost(self)
        ghost_width, ghost_height = ghost.rect.size
        available_space_x = self.settings.screen_width - (2 * ghost_width)
        number_ghosts_x = available_space_x // (2 * ghost_width)
        # Determine the number of rows of ghosts that fit on the screen.
        wizard_height = self.wizard.rect.height
        available_space_y = (self.settings.screen_height -
                             (3 * ghost_height)-wizard_height)
        number_rows = available_space_y // (2 * ghost_height)

        # Create the full crowd of ghosts
        for row_number in range(number_rows):
            for ghost_number in range(number_ghosts_x):
                self._create_ghost(ghost_number, row_number)

    def _create_ghost(self, ghost_number, row_number):
        # Create a ghost and place it in the row.
        ghost = Ghost(self)
        ghost_width, ghost_height = ghost.rect.size
        ghost.x = ghost_width + 2 * ghost_width * ghost_number
        ghost.rect.x = ghost.x
        ghost.rect.y = ghost.rect.height + 2 * ghost.rect.height * row_number
        self.ghosts.add(ghost)

    def _update_ghosts(self):
        """Update the positions of all ghosts in the crowd."""
        self._check_fleet_edges()
        self.ghosts.update()

        # Look for ghost-wizard collisions.
        if pygame.sprite.spritecollideany(self.wizard, self.ghosts):
            self._wizard_hit()
        # Look for ghosts hitting the bottom of the screen.
        self._check_ghosts_bottom()

    def _check_fleet_edges(self):
        """Respond appropriately if any ghosts have reached an edge."""
        for ghost in self.ghosts.sprites():
            if ghost.check_edges():
                self._change_crowd_direction()
                break

    def _change_crowd_direction(self):
        """Drop the entire crowd and change the crowd's direction."""
        for ghost in self.ghosts.sprites():
            ghost.rect.y += self.settings.crowd_drop_speed
        self.settings.crowd_direction *= -1

    def _wizard_hit(self):
        """Respond to the wizard being hit by an ghost."""
        if self.stats.wizards_left > 0:
            # Decrement wizard_left.
            self.stats.wizards_left -= 1
            # Get rid of any remaining ghosts and balls.
            self.ghosts.empty()
            self.balls.empty()
            # Create a new crowd and center the wizard.
            self._create_crowd()
            self.wizard.center_wizard()
            # Pause
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _check_ghosts_bottom(self):
        """Check if any ghosts have reached the bottom of the screen."""
        screen_rect = self.screen.get_rect()
        for ghost in self.ghosts.sprites():
            if ghost.rect.bottom >= screen_rect.bottom:
                # Treat this the same as if the wizard got hit.
                self._wizard_hit()
                break


if __name__ == '__main__':
    # Make a game instance, and run the game
    ga = GhostsAttack()
    ga.run_game()
