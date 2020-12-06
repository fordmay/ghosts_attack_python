class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.full_screen = False
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.FPS = 60

        # Wizard settings
        self.wizard_limit = 2

        # Ball settings
        self.ball_width = 10
        self.ball_height = 10
        self.balls_allowed = 3
        self.random_ball_color = True
        self.ball_color = (128, 0, 128)

        # ghost settings
        self.crowd_drop_speed = 10

        # How quickly the game speeds up
        self.speedup_scale = 2.0

        self.initialize_dynamic_settings()
        self.increase_speed()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.wizard_speed = 3.0
        self.ball_speed = 6.0
        self.ghost_speed = 2.0

        # crowd_direction of 1 represents right; -1 represents left.
        self.crowd_direction = 1

    def increase_speed(self):
        self.wizard_speed += self.speedup_scale
        self.ball_speed += self.speedup_scale
        self.ghost_speed += self.speedup_scale
