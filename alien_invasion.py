#Xavier Welker 20250309
#This file contains the logic for displaying screen, game staying on and getting some user inputs

import sys
import pygame
from settings import Settings
from ship import Ship

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

    def run_game(self):
        #Start the main loop for the game
        while True:
            #Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #redraw the screen during each pass through the loop
            self.screen.fill(self.settings.bg_color)

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