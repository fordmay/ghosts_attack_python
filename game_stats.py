class GameStats:
    """Track statistics for Ghosts Attack."""

    def __init__(self, ga_game):
        """Initialize statistics."""
        self.settings = ga_game.settings
        self.reset_stats()
        # High score should never be reset.
        self.high_score = 0
        # Start Ghosts Attack in an active state
        self.game_active = False

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.wizards_left = self.settings.wizard_limit
        self.score = 0
