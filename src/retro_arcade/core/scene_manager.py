"""Manage transitions between arcade scenes."""

from retro_arcade.core.scene import Scene


class SceneManager:
    """Manage the currently active scene."""

    def __init__(self) -> None:
        self._current_scene: Scene | None = None
        self.running = True

    @property
    def current_scene(self) -> Scene | None:
        """Return the active scene."""
        return self._current_scene

    def change_scene(self, scene: Scene) -> None:
        """Switch to another scene."""
        self._current_scene = scene

    def quit(self) -> None:
        """Request application shutdown."""
        self.running = False
