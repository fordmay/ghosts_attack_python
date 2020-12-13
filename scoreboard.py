import pygame.font
from heart import Heart
from pygame.sprite import Group


class Scoreboard:
    """A class to report scoring information."""

    def __init__(self, ga_game):
        self.screen = ga_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ga_game.settings
        self.stats = ga_game.stats

        # Font settings for scoring information.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare the initial score images.
        self.prep_score()
        self.prep_high_score()
        self.prep_hearts()

    def prep_score(self):
        """Turn the score into a rendered image."""
        score_str = "{:,}".format(self.stats.score)
        self.score_image = self.font.render(
            score_str, True, self.text_color, self.settings.bg_color)

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 10

    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        high_score = "{:,}".format(self.stats.high_score)
        self.high_score_image = self.font.render(
            high_score, True, self.text_color, self.settings.bg_color)

        # Center the high score at the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_hearts(self):
        """Show how many wizard's hearts are left."""
        self.hearts = Group()
        for wizard_number in range(self.stats.wizards_left):
            heart = Heart()
            heart.rect.x = 10 + wizard_number * heart.rect.width
            heart.rect.y = 10
            self.hearts.add(heart)

    def show_score(self):
        """Draw scores, and hearts to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.hearts.draw(self.screen)

    def check_high_score(self):
        """Check to see if there's a new high score."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
