#Xavier Welker 20250312
#this file trasks the statistic for the game alien invasion

class GameStats:
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        #high score should never be reset
        self.high_score = 0

    def reset_stats(self):
        #initialize statistics that can change during the game
        self.ships_left = self.settings.ship_limit
        self.score = 0