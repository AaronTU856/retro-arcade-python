"""Tests for arcade scene management."""

from retro_arcade.core.scene import Scene
from retro_arcade.core.scene_manager import SceneManager


class DummyScene(Scene):
    """Minimal scene used for testing."""

    def handle_event(self, event):
        pass

    def update(self, dt):
        pass

    def render(self, screen):
        pass


def test_initial_scene():
    manager = SceneManager()

    assert manager.current_scene is None


def test_initial_running_state():
    manager = SceneManager()

    assert manager.running is True


def test_change_scene():
    manager = SceneManager()
    scene = DummyScene()

    manager.change_scene(scene)

    assert manager.current_scene is scene


def test_switch_between_scenes():
    manager = SceneManager()

    first_scene = DummyScene()
    second_scene = DummyScene()

    manager.change_scene(first_scene)
    manager.change_scene(second_scene)

    assert manager.current_scene is second_scene


def test_quit():
    manager = SceneManager()

    manager.quit()

    assert manager.running is False
