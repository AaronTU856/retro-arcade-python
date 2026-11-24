from retro_arcade.core.settings import (
    FPS,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    TITLE,
)


def test_screen_dimensions():
    assert SCREEN_WIDTH > 0
    assert SCREEN_HEIGHT > 0


def test_frame_rate():
    assert FPS == 60


def test_application_title():
    assert TITLE == "Retro Arcade Python"
