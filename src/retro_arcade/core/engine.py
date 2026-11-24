"""Core arcade application engine."""

import pygame

from retro_arcade.core.scene_manager import SceneManager
from retro_arcade.core.settings import (
    BACKGROUND,
    FPS,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    TITLE,
)
from retro_arcade.ui.menu import MainMenu


class ArcadeEngine:
    """Manage the application lifecycle and game loop."""

    def __init__(self) -> None:
        pygame.init()

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(TITLE)

        self.clock = pygame.time.Clock()
        self.scene_manager = SceneManager()

        self.scene_manager.change_scene(MainMenu(self.scene_manager))

    def run(self) -> None:
        """Run the main application loop."""
        try:
            while self.scene_manager.running:
                dt = self.clock.tick(FPS) / 1000

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.scene_manager.quit()
                        break

                    scene = self.scene_manager.current_scene

                    if scene is not None:
                        scene.handle_event(event)

                    if not self.scene_manager.running:
                        break

                if not self.scene_manager.running:
                    break

                scene = self.scene_manager.current_scene

                if scene is not None:
                    scene.update(dt)

                    self.screen.fill(BACKGROUND)
                    scene.render(self.screen)

                pygame.display.flip()

        finally:
            pygame.quit()
