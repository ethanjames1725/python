"""Manages the ship's shield behaviour."""
import pygame
from pygame.sprite import Sprite


class Shield(Sprite):
    """A shield that blocks alien bullets in fron of the ship."""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.ship = ai_game.ship

        self.width = self.ship.rect.width + 20
        self.height = 12
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self._reposition()

        self.max_durability = self.settings.shield_max_durability
        self.durability = self.max_durability
        self.last_hit_time = 0

    def reset(self):
        """Fully restore the shield, matching the current difficulty."""
        self.max_durability = self.settings.shield_max_durability
        self.durability = self.max_durability
        self.last_hit_time = 0

    def _reposition(self):
        """Keep the shield centred just above the ship."""
        self.rect.centerx = self.ship.rect.centerx
        self.rect.bottom = self.ship.rect.top - 5

    @property
    def active(self):
        """The shield only blocks bullets while it has durability left."""
        return self.durability > 0

    def update(self):
        """Recharge passively over time and track the ship's position."""
        self._reposition()

        cooldown = (self.settings.shield_break_cd_ms if self.durability <= 0
                    else self.settings.shield_hit_cd_ms)
        if pygame.time.get_ticks() - self.last_hit_time < cooldown:
            return

        if self.durability < self.max_durability:
            self.durability = min(self.max_durability,
                self.durability + self.settings.shield_recharge_rate)

    def boost_recharge(self):
        """Speed up recharge as a reward for killing an alien."""
        boost = self.max_durability * self.settings.shield_recharge_boost
        self.durability = min(self.max_durability, self.durability + boost)

    def absorb_hit(self):
        """Recharge a hit from an alien bullet."""
        self.durability = max(0, self.durability - 1)
        self.last_hit_time = pygame.time.get_ticks()

    def draw(self):
        """Draw the shield as a bar that visually depletes."""
        if not self.active:
            return
        ratio = self.durability / self.max_durability
        fill_rect = pygame.Rect(
            self.rect.x, self.rect.y, int(self.width * ratio), self.height)

        pygame.draw.rect(self.screen, (0, 90, 160), self.rect,
                         border_radius=4)
        pygame.draw.rect(self.screen, (0, 220, 255), fill_rect,
                         border_radius=4)
        pygame.draw.rect(self.screen, (255, 255, 255), self.rect, 2,
                         border_radius=4)