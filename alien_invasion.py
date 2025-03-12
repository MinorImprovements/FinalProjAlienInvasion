#Xavier Welker 20250309
#This file contains the logic for displaying screen, game staying on and getting some user inputs

import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

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

        #create an instance of the group of aliens
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        #Start the main loop for the game
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
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

    #create the fleet of aliens
    def _create_fleet(self):
        alien = Alien(self)
        #spacing between aliens is one alien width and one alien height
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width

            #finished a row; reset x value and increment y value
            current_x = alien_width
            current_y += 2 * alien_height
        self.aliens.add(alien)


    #create alien and place it in row
    def _create_alien(self, x_position, y_posistion):
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_posistion
        self.aliens.add(new_alien)
    
    #Dropping fleet and changing directions
    def _check_fleet_edges(self):
        #respond appropriately if any aliens have reached an edge
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    #create and destroy bullets
    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        #check for any bullets that have hit aliens, if so, get rid of bullet and alien
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

    #update the positions of all aliens in the fleet
    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()


    #update images on the screen and flip to the new screen
    def _update_screen(self):
            #redraw the screen during each pass through the loop
            self.screen.fill(self.settings.bg_color)

            #loop through list of created bullets in group and draw that bullet to screen
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()

            #draw ship to screen
            self.ship.blitme()

            #draw alien to screen
            self.aliens.draw(self.screen)

            #Make the most recently drawn screen visible
            pygame.display.flip()

            #set frames per second
            self.clock.tick(60)

if __name__ == '__main__':
    #make game instance and run the game
    ai = Alieninvasion()
    ai.run_game()