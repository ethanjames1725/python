"""Pause menu: percentage volume buttons for Music and SFX, plus Resume/Main Menu."""
import pygame

from button import Button


class PauseMenu:
    """Overlay shown when the game is paused."""

    VOLUME_STEPS = (0.0, 0.25, 0.5, 0.75, 1.0)

    def __init__(self, ai_game):
        """Build the overlay, volume rows, and Resume/Main Menu buttons."""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings

        self.overlay = pygame.Surface(self.screen_rect.size, pygame.SRCALPHA)
        self.overlay.fill((0, 0, 0, 170))

        self.text_colour = (255, 255, 255)
        self.title_font = pygame.font.SysFont(None, 64)
        self.label_font = pygame.font.SysFont(None, 36)
        self.pct_font = pygame.font.SysFont(None, 28)

        self.title_image = self.title_font.render("Paused", True, self.text_colour)
        self.title_rect = self.title_image.get_rect()
        self.title_rect.centerx = self.screen_rect.centerx
        self.title_rect.centery = self.screen_rect.centery - 160

        self.music_row = self._build_volume_row("Music", -70)
        self.sfx_row = self._build_volume_row("SFX", 10)

        self.resume_button = Button(ai_game, "Resume", 100)
        self.main_menu_button = Button(ai_game, "Main Menu", 170)

    def _build_volume_row(self, label, y_offset):
        """Build a label plus a row of percentage buttons for one volume."""
        label_image = self.label_font.render(label, True, self.text_colour)
        label_rect = label_image.get_rect()
        label_rect.centerx = self.screen_rect.centerx
        label_rect.centery = self.screen_rect.centery + y_offset - 26

        button_width, button_height, gap = 70, 34, 10
        row_width = (len(self.VOLUME_STEPS) * button_width
                + (len(self.VOLUME_STEPS) - 1) * gap)
        start_x = self.screen_rect.centerx - row_width // 2

        buttons = []
        for i, step in enumerate(self.VOLUME_STEPS):
            rect = pygame.Rect(0, 0, button_width, button_height)
            rect.x = start_x + i * (button_width + gap)
            rect.centery = self.screen_rect.centery + y_offset
            buttons.append((step, rect))

        return {'label_image': label_image, 'label_rect': label_rect,
                'buttons': buttons}

    def _draw_row(self, row, current_value):
        self.screen.blit(row['label_image'], row['label_rect'])
        for step, rect in row['buttons']:
            colour = (0, 135, 0) if step == current_value else (70, 70, 70)
            pygame.draw.rect(self.screen, colour, rect, border_radius=4)
            pct_image = self.pct_font.render(f"{int(step * 100)}%", True,
                    self.text_colour)
            pct_rect = pct_image.get_rect(center=rect.center)
            self.screen.blit(pct_image, pct_rect)

    def draw(self):
        """Draw the pause overlay, volume rows, and Resume/Main Menu buttons."""
        self.screen.blit(self.overlay, (0, 0))
        self.screen.blit(self.title_image, self.title_rect)
        self._draw_row(self.music_row, self.settings.music_volume)
        self._draw_row(self.sfx_row, self.settings.sfx_volume)
        self.resume_button.draw_button()
        self.main_menu_button.draw_button()

    def check_click(self, mouse_pos):
        """Handle a mouse click anywhere on the pause menu."""
        for step, rect in self.music_row['buttons']:
            if rect.collidepoint(mouse_pos):
                self.settings.music_volume = step
                pygame.mixer.music.set_volume(step)
                return

        for step, rect in self.sfx_row['buttons']:
            if rect.collidepoint(mouse_pos):
                self.settings.sfx_volume = step
                self.ai_game.apply_sfx_volume()
                return

        if self.resume_button.rect.collidepoint(mouse_pos):
            self.ai_game._toggle_pause()
        elif self.main_menu_button.rect.collidepoint(mouse_pos):
            self.ai_game._return_to_main_menu()
