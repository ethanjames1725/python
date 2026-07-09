"""Stores all settings in one module."""

class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialises the game's static settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (135, 206, 235)

        # Bullet settings
        self.bullet_width = 4
        self.bullet_height = 15
        self.bullet_colour = (255, 60, 60)

        # Boost settings
        self.boost_mult = 2.0
        self.boost_max_fuel = 100
        self.boost_drain_rate = 2
        self.boost_regen_rate = 2

        # How quickly the game speeds up
        self.speedup_scale = 1.1

        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialise_dynamic_settings()

    def initialise_dynamic_settings(self):
        """Initialise settings that change throughout the game."""
        self.ship_speed = 2.0
        self.bullet_speed = 5.0
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.bullets_allowed = 3
        self.ship_limit = 3

        # fleet direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Scoring settings
        self.alien_points = 50

    def set_easy(self):
        """Set difficulty attributes for easy mode."""
        self.initialise_dynamic_settings()
        self.ship_speed = 2.5
        self.alien_speed = 0.7
        self.fleet_drop_speed = 5
        self.bullets_allowed = 5
        self.ship_limit = 4

    def set_medium(self):
        """Set difficulty attributes for medium mode."""
        self.initialise_dynamic_settings()

    def set_hard(self):
        """Set difficulty attributes for hard mode."""
        self.initialise_dynamic_settings()
        self.ship_speed = 1.5
        self.alien_speed = 1.5
        self.fleet_drop_speed = 15
        self.bullets_allowed = 2
        self.ship_limit = 2

    def increase_speed(self):
        """Increase speed settings and alien point value."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
