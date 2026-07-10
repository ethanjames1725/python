"""Manages bullets fired by aliens."""
import pygame
from pygame.sprite import Sprite


class AlienBullet(Sprite):
    """A class to manage bullets fired by aliens toward the ship."""

    def __init__(self, ai_game, alien):
        """Create an alien bullet at the given alien's position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.colour = (255, 200, 0)

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
            self.settings.bullet_height)
        self.rect.midtop = alien.rect.midbottom

        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet down the screen."""
        self.y += self.settings.alien_bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.colour, self.rect)
