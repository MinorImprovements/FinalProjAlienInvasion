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
        self.prep_high_score()

    #turn the scoreboard into a rendered image
    def prep_score(self):
        rounded_score = round(self.stats.score, -1)
        score_str = f"{rounded_score:,}"
        self.score_image = self.font.render(f"Score: {score_str}", True, self.text_color, self.settings.bg_color)

        #display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right  = self.screen_rect.right - 20
        self.score_rect_top = 20

    #turn hihg score into a rendered image
    def prep_high_score(self):
        high_score = round(self.stats.high_score, -1)
        high_score_str = f"Top Socre: {high_score:,}"
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)

        #center the high score at the top of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    #draw score to screen
    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)

    #check to see if there is a new high score
    def check_high_score(self):
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()