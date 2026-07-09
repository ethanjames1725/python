"""Main class that runs the Alien Invasion game."""
import sys
from time import sleep
from pathlib import Path

import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    """Overall class to manage game assets and behaviour."""

    def __init__(self):
        """Initialises the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        # Load and scale the space background to fill the screen.
        bg_path = Path(__file__).parent/'images'/'space_bg.jpg'
        self.bg_image = pygame.image.load(bg_path)
        self.bg_image = pygame.transform.scale(self.bg_image,
            (self.settings.screen_width, self.settings.screen_height)
        )

        # Load sound effects
        self.shoot_sound = self._load_sound('shoot.wav')
        self.explosion_sound = self._load_sound('explosion.wav')
        self.ship_hit_sound = self._load_sound('ship_hit.wav')

        # Create an instance to store game statistics,
        # and create a scoreboard.
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # Start Alien Invasion in an inactive state.
        self.game_active = False

        # Makes three difficulty buttons.
        self.easy_button = Button(self, "Easy", -100)
        self.medium_button = Button(self, "Medium")
        self.hard_button = Button(self, "Hard", 100)

        # Remember the last difficulty chosen, so 'P' can replay it.
        self.last_difficulty = self.settings.set_medium

    def _load_sound(self, file_name):
        """
        Load a sound effectm returning None if the file is not found yet.
        """
        sound_path = Path(__file__).parent/'sounds'/file_name
        try:
            return pygame.mixer.Sound(sound_path)
        except (FileNotFoundError, pygame.error):
            return None

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._exit_game()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_difficulty_buttons(mouse_pos)

    def _exit_game(self):
        """Save the high score and quit."""
        self.stats.save_high_score()
        sys.exit()

    def _check_difficulty_buttons(self, mouse_pos):
        """Start a new game at the chosen difficulty."""
        if self.game_active:
            return

        if self.easy_button.rect.collidepoint(mouse_pos):
            self.last_difficulty = self.settings.set_easy
            self.last_difficulty()
            self._start_game()
        elif self.medium_button.rect.collidepoint(mouse_pos):
            self.last_difficulty = self.settings.set_medium
            self.last_difficulty()
            self._start_game()
        elif self.hard_button.rect.collidepoint(mouse_pos):
            self.last_difficulty = self.settings.set_hard
            self.last_difficulty()
            self._start_game()

    def _start_game(self):
        """Reset game state and start a new game."""
        # Reset the game settings.
        self.stats.reset_stats()
        self.sb.prep_images()
        self.game_active = True

        # Get rid of any remaining bullets and aliens.
        self.bullets.empty()
        self.aliens.empty()

        # Create a new fleet and center the ship.
        self._create_fleet()
        self.ship.centre_ship()

        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_LSHIFT:
            self.ship.boosting = True
        elif event.key == pygame.K_q:
            self._exit_game()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_p:
            self.last_difficulty()
            self._start_game()
        elif event.key == pygame.K_ESCAPE:
            self.game_active = False
            pygame.mouse.set_visible(True)

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_LSHIFT:
            self.ship.boosting = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            if self.shoot_sound:
                self.shoot_sound.play()

    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Create an alien and keep adding aliens until there's no room left.
        # Spacing between aliens is one alien width and one alien height.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width

            # Finished a row; reset x value, and increment y value.
            current_x = alien_width
            current_y += 2 * alien_height

    def _create_alien(self, x_position, y_position):
        """Create an alien and place it in the fleet."""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _check_bullet_alien_collisions(self):
        """Respond to any bullet-alien collisions."""
        # Remove any bullets and aliens that have collided.
        collisions = pygame.sprite.groupcollide(
                self.bullets, self.aliens, True, True)

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
            if self.explosion_sound:
                self.explosion_sound.play()

        if not self.aliens:
            self._start_new_level()

    def _start_new_level(self):
        """
        Clear existing bullets, create a new fleet, and speed up the game.
        """
        self.bullets.empty()
        self._create_fleet()
        self.settings.increase_speed()

        # Increase level.
        self.stats.level += 1
        self.sb.prep_level()

    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen."""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                # Treat this the same as if the ship got hit.
                self._ship_hit()
                break

    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        if self.ship_hit_sound:
            self.ship_hit_sound.play()
        if self.stats.ships_left > 0:
            # Decrement ships_left, and update scoreboard.
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            # Get rid of any remaining bullets and aliens.
            self.bullets.empty()
            self.aliens.empty()

            # Create a new fleet and centre the ship.
            self._create_fleet()
            self.ship.centre_ship()
            #Pause
            sleep(0.5)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)

    def _change_fleet_direction(self):
        """Drop the entire fleet and change their direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_aliens(self):
        """Check if the fleet is at an edge, then update positions."""
        self._check_fleet_edges()
        self.aliens.update()

        # Look for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Look for aliens hitting the bottom of the screen.
        self._check_aliens_bottom()

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.blit(self.bg_image, (0, 0))
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.ship.draw_boost_bar()
        self.aliens.draw(self.screen)

        # Draw the score information.
        self.sb.show_score()

        # Draw the play button if the game is inactive.
        if not self.game_active:
            self.easy_button.draw_button()
            self.medium_button.draw_button()
            self.hard_button.draw_button()

        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
