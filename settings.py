#Xavier Welker 20250309
#creates a settings object to create easy modification to game appearnce and behavior

class Settings:
    #A class to store all settings for Alien Invasion
    def __init__(self):
        #Initialize the game's settings

        #screen settings
        self.screen_width = 1250
        self.screen_height = 1080
        self.bg_color = (230,230,230)
