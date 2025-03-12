#Xavier Welker 20250309
#This file contains the logic for displaying screen, game staying on and getting some user inputs

import sys
from time import sleep
import pygame
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
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

        #create an instance to store game statistics and create scoreboard
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        #create an inastance of the Ship class
        self.ship = Ship(self)

        #create group that hold bullets
        self.bullets = pygame.sprite.Group()

        #create an instance of the group of aliens
        self.aliens = pygame.sprite.Group()

        #start Alien Invasion in an active state
        self.game_active = False
        
        #create the play button
        self.play_button = Button(self, "Play")

        self._create_fleet()

    def run_game(self):
        #Start the main loop for the game
        while True:
            self._check_events()
            if self.game_active:
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    #start a new game when the player clicks play
    def _check_play_button(self, mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            #reset game settings
            self.settings.initialize_dynamic_settings()
            #reset game statistics
            self.stats.reset_stats()
            self.sb.prep_score()
            self.sb.prep_level()
            self.game_active = True

            #Get rid of any remaining bullets and aliens
            self.bullets.empty()
            self.aliens.empty()

            #Create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()

            #hide the mouse cursor
            pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        #respond to keypresses
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            #move the ship to the right.
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
             #move ship to left
            self.ship.moving_left = True
        #check if Q is pressed
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    
    def _check_keyup_events(self, event):
        #respond to keyreleases
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a: 
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

        self._check_bullet_alien_collisions()
    
    def _check_bullet_alien_collisions(self):
        #check for any bullets that have hit aliens, if so, get rid of bullet and alien
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            #increase level
            self.stats.level += 1
            self.sb.prep_level()

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

    #update the positions of all aliens in the fleet
    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()
        #look for alien-ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        self._check_aliens_bottom()

    #respnd to the ship being hit by an alien
    def _ship_hit(self):
        if self.stats.ships_left > 0:
            #decrement ships left
            self.stats.ships_left -= 1
            #remove any remaining bullets and anliens
            self.bullets.empty()
            self.aliens.empty()
            #create new fleet and center ship
            self._create_fleet()
            self.ship.center_ship()
            #pause
            sleep(0.5)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)

    #check if aliens have reached the bottom of the screen
    def _check_aliens_bottom(self):
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                self._ship_hit()
                break


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

            #draw the score info
            self.sb.show_score()

            #Draw play button if the game is inactive
            if not self.game_active:
                self.play_button.draw_button()

            #Make the most recently drawn screen visible
            pygame.display.flip()

            #set frames per second
            self.clock.tick(60)

if __name__ == '__main__':
    #make game instance and run the game
    ai = Alieninvasion()
    ai.run_game()