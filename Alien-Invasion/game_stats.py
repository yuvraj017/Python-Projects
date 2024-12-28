class GameStats:
    """Track statistics for AI players."""
    def __init__(self, ai_game):
        """Initialize statistics for AI player. """
        self.settings = ai_game.settings
        self.reset_stats()
        
        # Start alien invasion in an active state.
        self.game_active = True

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit