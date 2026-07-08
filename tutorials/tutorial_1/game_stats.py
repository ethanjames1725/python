"""Track statistics for Alien Invasion."""
import json
from pathlib import Path


class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialise statistics."""
        self.settings = ai_game.settings
        self.high_score_file = Path(__file__).parent/'high_score.json'
        self.reset_stats()

        # High score should never be reset
        self.high_score = self._read_high_score()

    def reset_stats(self):
        """Initialise statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def _read_high_score(self):
        """Read the saved high score from file, if it exists."""
        if self.high_score_file.exists():
            contents = self.high_score_file.read_text()
            if contents:
                return json.loads(contents)
        return 0

    def save_high_score(self):
        """Save the current high score to file."""
        contents = json.dumps(self.high_score)
        self.high_score_file.write_text(contents)
