"""Temporary screen for features under development."""

from collections.abc import Callable

import pygame

from retro_arcade.core.scene import Scene
from retro_arcade.core.settings import (
    GREY,
    NEON_GREEN,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    WHITE,
)


class PlaceholderScene(Scene):
    """Display a temporary feature screen."""

    def __init__(
        self,
        title: str,
        on_back: Callable[[], None],
    ) -> None:
        self.title = title
        self.on_back = on_back

        self.title_font = pygame.font.Font(None, 64)
        self.text_font = pygame.font.Font(None, 30)

    def handle_event(self, event: pygame.event.Event) -> None:
        """Return to the menu when Escape is pressed."""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.on_back()

    def update(self, dt: float) -> None:
        """Update the placeholder scene."""

    def render(self, screen: pygame.Surface) -> None:
        """Draw the placeholder screen."""
        title = self.title_font.render(self.title, True, NEON_GREEN)

        message = self.text_font.render("Coming Soon", True, WHITE)

        instructions = self.text_font.render("Press ESC to return", True, GREY)

        screen.blit(
            title,
            title.get_rect(center=(SCREEN_WIDTH // 2, 220)),
        )

        screen.blit(
            message,
            message.get_rect(center=(SCREEN_WIDTH // 2, 300)),
        )

        screen.blit(
            instructions,
            instructions.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 60)),
        )
