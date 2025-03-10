#Xavier Welker 20250309
#This file contains the logic for displaying screen, game staying on and getting some user inputs

import sys
import pygame

class Alieninvasion:
    #Overall class to manage game assets and behavior

    def __init__(self):
        #Initialize the game and create game resources
        pygame.init()

        #crate a instance of the Clock class to controll the frame rate
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((1250,1080))
        pygame.display.set_caption("Alien Invasion")

        #set the background color
        self.bg_color = (230,230,230)

    def run_game(self):
        #Start the main loop for the game
        while True:
            #Watch for keyboard and mouse events
            for event in pygame.evet.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #redraw the screen during each pass through the loop
            self.screen.fill(self.bg_color)

            #Make the most recently drawn screen visible
            pygame.display.flip()

            #set frames per second
            self.clock.tick(60)

if __name__ == '__main__':
    #make game instance and run the game
    ai = AlienInvasion()
    ai.run_game()