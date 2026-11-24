"""Main menu for the Retro Arcade application."""

import pygame

from retro_arcade import __version__
from retro_arcade.core.scene import Scene
from retro_arcade.core.scene_manager import SceneManager
from retro_arcade.core.settings import (
    GREY,
    NEON_GREEN,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    WHITE,
)
from retro_arcade.ui.placeholder import PlaceholderScene


class MainMenu(Scene):
    """Display and manage the arcade main menu."""

    def __init__(self, scene_manager: SceneManager) -> None:
        self.scene_manager = scene_manager

        self.options = [
            "Play Snake",
            "High Scores",
            "Settings",
            "Exit",
        ]

        self.selected_index = 0

        self.title_font = pygame.font.Font(None, 80)
        self.menu_font = pygame.font.Font(None, 38)
        self.small_font = pygame.font.Font(None, 24)

    def handle_event(self, event: pygame.event.Event) -> None:
        """Process menu navigation."""

        if event.type != pygame.KEYDOWN:
            return

        if event.key in (pygame.K_UP, pygame.K_w):
            self.selected_index = (self.selected_index - 1) % len(self.options)

        elif event.key in (pygame.K_DOWN, pygame.K_s):
            self.selected_index = (self.selected_index + 1) % len(self.options)

        elif event.key in (pygame.K_RETURN, pygame.K_SPACE):
            self.select_option()

        elif event.key == pygame.K_ESCAPE:
            self.scene_manager.quit()

    def select_option(self) -> None:
        """Open the selected menu option."""
        selected = self.options[self.selected_index]

        if selected == "Exit":
            self.scene_manager.quit()
            return

        self.scene_manager.change_scene(
            PlaceholderScene(
                title=selected,
                on_back=self.return_to_menu,
            )
        )

    def return_to_menu(self) -> None:
        """Restore the main menu."""
        self.scene_manager.change_scene(self)

    def update(self, dt: float) -> None:
        """Update the menu state."""

    def render(self, screen: pygame.Surface) -> None:
        """Render the main menu."""
        title = self.title_font.render("RETRO ARCADE", True, NEON_GREEN)

        subtitle = self.small_font.render("PYTHON GAMING PLATFORM", True, GREY)

        screen.blit(
            title,
            title.get_rect(center=(SCREEN_WIDTH // 2, 100)),
        )

        screen.blit(
            subtitle,
            subtitle.get_rect(center=(SCREEN_WIDTH // 2, 150)),
        )

        for index, option in enumerate(self.options):
            selected = index == self.selected_index

            colour = NEON_GREEN if selected else WHITE
            border_colour = NEON_GREEN if selected else GREY

            button = pygame.Rect(0, 0, 400, 55)
            button.center = (
                SCREEN_WIDTH // 2,
                225 + index * 75,
            )

            pygame.draw.rect(
                screen,
                border_colour,
                button,
                width=2,
                border_radius=5,
            )

            label = self.menu_font.render(option.upper(), True, colour)

            screen.blit(
                label,
                label.get_rect(center=button.center),
            )

            if selected:
                arrow = self.menu_font.render(">", True, NEON_GREEN)

                screen.blit(
                    arrow,
                    (button.left - 35, button.top + 10),
                )

        instructions = self.small_font.render(
            "UP / DOWN: Navigate | ENTER: Select | ESC: Exit",
            True,
            GREY,
        )

        screen.blit(
            instructions,
            instructions.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 70)),
        )

        version = self.small_font.render(f"v{__version__}", True, GREY)

        screen.blit(
            version,
            version.get_rect(
                bottomright=(
                    SCREEN_WIDTH - 15,
                    SCREEN_HEIGHT - 15,
                )
            ),
        )
