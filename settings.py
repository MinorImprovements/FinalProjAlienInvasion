#Xavier Welker 20250309
#creates a settings object to create easy modification to game appearnce and behavior

class Settings:
    #A class to store all settings for Alien Invasion
    def __init__(self):
        #Initialize the game's settings

        #screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (115,215,255)
        self.ship_image = 'images/ship.bmp'
        self.ship_speed = 5
