"""Manages most of the behaviour of the player's ship."""
import pygame
from pygame.sprite import Sprite
from pathlib import Path


class Ship(Sprite):
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialise the ship and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        image_path = Path(__file__).parent/'images'/'ship.bmp'
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom centre of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a float for the ship's exact horizontal position.
        self.x = float(self.rect.x)

        # Movement flag; start with a ship that's not moving.
        self.moving_right = False
        self.moving_left = False
        self.boosting = False
        self.boost_fuel = self.settings.boost_max_fuel

    def update(self):
        """Update the ship's position based on the movement flag."""
        speed = self.settings.ship_speed
        if self.boosting and self.boost_fuel > 0:
            speed *= self.settings.boost_mult
            self.boost_fuel -= self.settings.boost_drain_rate
        else:
            self.boost_fuel += self.settings.boost_regen_rate

        self.boost_fuel = max(0, min(self.settings.boost_max_fuel,
                                     self.boost_fuel))

        # Update the ship's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += speed
        if self.moving_left and self.rect.left > 0:
            self.x -= speed

        # Update rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def centre_ship(self):
        """Centre the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def draw_boost_bar(self):
        """Draw a bar showing current boost fuel."""
        fuel_ratio = self.boost_fuel / self.settings.boost_max_fuel
        bar_width, bar_height = 200, 20
        bar_x = 20
        bar_y = self.screen_rect.bottom - bar_height - 20

        bg_rect = pygame.Rect(bar_x, bar_y, bar_width, bar_height)
        fill_rect = pygame.Rect(
            bar_x, bar_y, bar_width * fuel_ratio, bar_height)

        pygame.draw.rect(self.screen, (60, 60, 60), bg_rect)
        pygame.draw.rect(self.screen, (0, 200, 255), fill_rect)
        pygame.draw.rect(self.screen, (255, 255, 255), bg_rect, 2)
