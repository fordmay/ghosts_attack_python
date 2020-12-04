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
        self.wizard_speed = 4.0

        # Ball settings
        self.ball_speed = 2.0
        self.ball_width = 10
        self.ball_height = 10
        self.balls_allowed = 5
        self.random_ball_color = True
        self.ball_color = (128, 0, 128)

        # ghost settings
        self.ghost_speed = 2.0
        self.crowd_drop_speed = 10
        # crowd_direction of 1 represents right; -1 represents left.
        self.crowd_direction = 1
