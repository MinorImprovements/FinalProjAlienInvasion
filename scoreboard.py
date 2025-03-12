#Xavier Welker 20250312
#This file contains the Scoreboard class

import pygame.font

#This class reports scoring information
class Scoreboard:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        #Font settings for scoring info
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        #prepare initial score image
        self.prep_score()

    #turn the scoreboard into a rendered image
    def prep_score(self):
        score_str = str(self.stats.score)
        self.score_image = self.font.render(f"Score: {score_str}", True, self.text_color, self.settings.bg_color)

        #display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right  = self.screen_rect.right - 20
        self.score_rect_top = 20

    #draw score to screen
    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)