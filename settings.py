class Settings:
    """A class that stores settings for game Alien Invasion"""

    def __init__(self):
        # Screen settings
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (102, 0, 161)

        # Ship Settings
        self.ship_speed_factor = 0.5

        # Bullet Settings
        self.bullet_speed_factor = 0.5
        self.bullet_width = 3
        self.bullet_hight = 15
        self.bullet_color = 255, 0, 0