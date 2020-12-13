class GameStats:
    """Track statistics for Ghosts Attack."""

    def __init__(self, ga_game):
        """Initialize statistics."""
        self.settings = ga_game.settings
        self.reset_stats()

        # High score should never be reset.
        self.high_score = self._read_high_score()
        # Start Ghosts Attack in an active state
        self.game_active = False

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.wizards_left = self.settings.wizard_limit
        self.score = 0

    def _read_high_score(self):
        """Read high score from file or create it"""
        try:
            with open('high_score.txt', 'r') as f:
                high_score_content = int(f.read())
        except (FileNotFoundError, ValueError):
            with open('high_score.txt', 'w') as f:
                f.write("0")
                high_score_content = 0
        return high_score_content

    def write_high_score(self):
        """Write high score to file"""
        with open('high_score.txt', 'w') as f:
            f.write(str(self.high_score))
