"""Main entry point for the Retro Arcade application."""

import pygame

from retro_arcade.core.settings import (
    BACKGROUND,
    FPS,
    GREY,
    NEON_GREEN,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    TITLE,
    WHITE,
)


def main():
    """Initialise and run the arcade application."""
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(TITLE)

    clock = pygame.time.Clock()

    title_font = pygame.font.Font(None, 72)
    subtitle_font = pygame.font.Font(None, 30)

    title_surface = title_font.render("RETRO ARCADE", True, NEON_GREEN)

    subtitle_surface = subtitle_font.render("Python Gaming Platform", True, WHITE)

    exit_surface = subtitle_font.render("Press ESC to exit", True, GREY)

    running = True

    try:
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

            screen.fill(BACKGROUND)

            screen.blit(
                title_surface,
                title_surface.get_rect(center=(SCREEN_WIDTH // 2, 220)),
            )

            screen.blit(
                subtitle_surface,
                subtitle_surface.get_rect(center=(SCREEN_WIDTH // 2, 280)),
            )

            screen.blit(
                exit_surface,
                exit_surface.get_rect(center=(SCREEN_WIDTH // 2, 550)),
            )

            pygame.display.flip()
            clock.tick(FPS)

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
