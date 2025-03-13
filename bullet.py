#Xavier Welker 20250310
#This file contains the bullet class

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    #A class to manage bullets fired from the ship
    def __init__(self, ai_game):
        #create a bullet object at the ship's current position
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #create a bullet rect at (0,0) and then set correct position
        self.image = pygame.image.load(self.settings.bullet_image).convert()
        #change the background of the image with the below RGB value to the same color as screen background
        self.image.set_colorkey((230,230,230))
        self.rect = self.image.get_rect()
        self.rect.midtop = ai_game.ship.rect.midtop

        #store the bullet's position as a float
        self.y = float(self.rect.y)

    def update(self):
        #move the bullet up the screen and update the exact position of the bullet
        self.y -= self.settings.bullet_speed
        #update rect position
        self.rect.y = self.y

    def draw_bullet(self):
        #draw the bullet to the screen
        self.screen.blit(self.image, self.rect)