"""Base class for all arcade scenes."""

from abc import ABC, abstractmethod

import pygame


class Scene(ABC):
    """Define the interface shared by all scenes."""

    @abstractmethod
    def handle_event(self, event: pygame.event.Event) -> None:
        """Process application events."""

    @abstractmethod
    def update(self, dt: float) -> None:
        """Update scene state."""

    @abstractmethod
    def render(self, screen: pygame.Surface) -> None:
        """Render the screen to display."""
