#Xavier Welker 20250309
#creates a settings object to create easy modification to game appearnce and behavior

class Settings:
    #A class to store all settings for Alien Invasion
    def __init__(self):
        #Initialize the game's static settings settings

        #screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (115,215,255)

        #ship settings
        self.ship_image = 'images/boy.bmp'
        self.ship_speed = 7
        self.ship_limit = 3

        #Bullet settings
        self.bullet_speed = 7.0
        self.bullet_image = 'images/hamburger.bmp'

        #alien settings
        self.alien_image = 'images/zombie.bmp'
        self.fleet_drop_speed = 7
        #fleet_direction of 1 reoresents right; -1 represents left
        self.fleet_direction = 1

        #initialize game's dynamic settings

        #how quickly game speeds up
        self.speedup_scale = 1.1
        #how points scale up as levels increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    #resetting speeds on game reset
    def initialize_dynamic_settings(self):
        self.alien_speed = 2
        self.alien_points = 50
        
    #increase speed settings
    def increase_speed(self):
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.score_scale * self.alien_points)
