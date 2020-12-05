class GameStats:
    """Track statistics for Ghosts Attack."""

    def __init__(self, ga_game):
        """Initialize statistics."""
        self.settings = ga_game.settings
        self.reset_stats()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.wizards_left = self.settings.wizard_limit