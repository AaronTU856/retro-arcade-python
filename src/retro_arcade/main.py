"""Main entry point for Retro Arcade."""

from retro_arcade.core.engine import ArcadeEngine


def main() -> None:
    """Launch the arcade application."""
    engine = ArcadeEngine()
    engine.run()


if __name__ == "__main__":
    main()
