

class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.FPS = 60

        # Wizard settings
        self.wizard_speed = 8.0

        # Ball settings
        self.ball_speed = 5.0
        self.ball_width = 10
        self.ball_height = 10
        self.balls_allowed = 5
