#Xavier Welker 20250309
#This file contains the logic for displaying screen, game staying on and getting some user inputs

import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

class Alieninvasion:
    #Overall class to manage game assets and behavior

    def __init__(self):
        #Initialize the game and create game resources
        pygame.init()

        #crate a instance of the Clock class to controll the frame rate
        self.clock = pygame.time.Clock()

        #creating an instance of the settings class to manipulate game settings from one file
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        #create an inastance of the Ship class
        self.ship = Ship(self)

        #create group that hold bullets
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        #Start the main loop for the game
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()

            #get rid of bullets that have disappeared
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)

            self._update_screen()
            
    def _check_events(self):
        #Watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        #respond to keypresses
        if event.key == pygame.K_RIGHT:
            #move the ship to the right.
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
             #move ship to left
            self.ship.moving_left = True
        #check if Q is pressed
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    
    def _check_keyup_events(self, event):
        #respond to keyreleases
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT: 
            self.ship.moving_left = False

    #create a new bullet and add it to the bullets group
    def _fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    #update images on the screen and flip to the new screen
    def _update_screen(self):
            #redraw the screen during each pass through the loop
            self.screen.fill(self.settings.bg_color)

            #loop through list of created bullets in group and draw that bullet to screen
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()

            #draw ship to screen
            self.ship.blitme()

            #Make the most recently drawn screen visible
            pygame.display.flip()

            #set frames per second
            self.clock.tick(60)

if __name__ == '__main__':
    #make game instance and run the game
    ai = Alieninvasion()
    ai.run_game()