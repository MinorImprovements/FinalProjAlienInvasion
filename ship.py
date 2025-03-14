#Xavier Welker 20250310
#This file contains the ship class that controls starting position and image

import pygame
from pygame.sprite import Sprite
from settings import Settings

class Ship(Sprite):
    #A class to manage the ship
    def __init__(self, ai_game):
        super().__init__()
        #Initialize the ship and set its starting position
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #using instance of the Settings class from alien_invasion.py to modify settings
        self.settings = ai_game.settings

        #Load the ship image, make the background transparent and get its rect
        self.image = pygame.image.load(self.settings.ship_image).convert()
        #change the background of the image with the below RGB value to the same color as screen background
        self.image.set_colorkey((230,230,230))
        self.rect = self.image.get_rect()

        #start each new ship at the bottome center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        #store a float for the ship's exact horizontal position
        self.x = float(self.rect.x)

        #Movement flag; start with a ship that's not moving
        self.moving_right = False
        self.moving_left = False

    def update(self):
        #Update the ship's position based on the movement flag
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        #update rect object from self.x
        self.rect.x = self.x

    #Center the ship on screen
    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def blitme(self):
        #Draw the ship at its current location
        self.screen.blit(self.image, self.rect)