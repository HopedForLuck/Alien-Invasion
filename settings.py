class Settings:
    """A class that stores settings for game Alien Invasion"""

    def __init__(self):
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (102, 0, 161)

        # Ship Settings
        self.ship_speed_factor = 0.5

        # Bullet Settings
        self.bullet_speed_factor = 0.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 255, 0, 0
        self.bullets_allowed = 3
