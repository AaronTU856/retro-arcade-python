"""Pygame scene for the Snake game."""

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
from retro_arcade.games.snake.config import (
    BOARD_COLOUR,
    BOARD_HEIGHT,
    BOARD_TOP,
    BOARD_WIDTH,
    CELL_SIZE,
    FOOD_COLOUR,
    GRID_COLOUR,
    HEAD_COLOUR,
    SNAKE_COLOUR,
)
from retro_arcade.games.snake.logic import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    SnakeLogic,
)


class SnakeGame(Scene):
    """Render and control the Snake game."""

    def __init__(self, on_back: Callable[[], None]) -> None:
        self.on_back = on_back
        self.logic = SnakeLogic()

        self.elapsed_time = 0.0
        self.started = False

        self.board_left = (SCREEN_WIDTH - BOARD_WIDTH) // 2

        self.title_font = pygame.font.Font(None, 64)
        self.text_font = pygame.font.Font(None, 32)
        self.small_font = pygame.font.Font(None, 24)

    def handle_event(self, event: pygame.event.Event) -> None:
        """Process keyboard input."""
        if event.type != pygame.KEYDOWN:
            return

        if event.key == pygame.K_ESCAPE:
            self.on_back()
            return

        if event.key == pygame.K_r:
            self.logic.reset()
            self.elapsed_time = 0.0
            self.started = False
            return

        if event.key == pygame.K_p and self.started:
            self.logic.toggle_pause()
            self.elapsed_time = 0.0
            return

        if self.logic.game_over or self.logic.paused:
            return

        directions = {
            pygame.K_UP: UP,
            pygame.K_w: UP,
            pygame.K_DOWN: DOWN,
            pygame.K_s: DOWN,
            pygame.K_LEFT: LEFT,
            pygame.K_a: LEFT,
            pygame.K_RIGHT: RIGHT,
            pygame.K_d: RIGHT,
        }

        if event.key in directions:
            self.logic.change_direction(directions[event.key])
            self.started = True

    def update(self, dt: float) -> None:
        """Update movement independently of frame rate."""
        if not self.started or self.logic.paused or self.logic.game_over:
            return

        self.elapsed_time += min(dt, 0.25)

        while not self.logic.game_over:
            interval = 1 / self.logic.speed

            if self.elapsed_time < interval:
                break

            self.elapsed_time -= interval
            self.logic.move()

    def draw_board(self, screen: pygame.Surface) -> None:
        """Draw the playing area and grid."""
        board = pygame.Rect(
            self.board_left,
            BOARD_TOP,
            BOARD_WIDTH,
            BOARD_HEIGHT,
        )

        pygame.draw.rect(screen, BOARD_COLOUR, board)

        for x in range(
            self.board_left,
            self.board_left + BOARD_WIDTH,
            CELL_SIZE,
        ):
            pygame.draw.line(
                screen,
                GRID_COLOUR,
                (x, BOARD_TOP),
                (x, BOARD_TOP + BOARD_HEIGHT),
            )

        for y in range(
            BOARD_TOP,
            BOARD_TOP + BOARD_HEIGHT,
            CELL_SIZE,
        ):
            pygame.draw.line(
                screen,
                GRID_COLOUR,
                (self.board_left, y),
                (self.board_left + BOARD_WIDTH, y),
            )

        pygame.draw.rect(
            screen,
            NEON_GREEN,
            board,
            width=1,
        )

    def draw_cell(
        self,
        screen: pygame.Surface,
        position: tuple[int, int],
        colour: tuple[int, int, int],
    ) -> None:
        """Convert grid coordinates into screen coordinates."""
        x, y = position

        rect = pygame.Rect(
            self.board_left + x * CELL_SIZE + 1,
            BOARD_TOP + y * CELL_SIZE + 1,
            CELL_SIZE - 2,
            CELL_SIZE - 2,
        )

        pygame.draw.rect(
            screen,
            colour,
            rect,
            border_radius=3,
        )

    def draw_hud(self, screen: pygame.Surface) -> None:
        """Display the title, score and level."""
        title = self.title_font.render("SNAKE", True, NEON_GREEN)

        score = self.text_font.render(f"Score: {self.logic.score}", True, WHITE)

        level = self.text_font.render(f"Level: {self.logic.level}", True, WHITE)

        screen.blit(
            title,
            title.get_rect(center=(SCREEN_WIDTH // 2, 45)),
        )

        screen.blit(
            score,
            (self.board_left, 85),
        )

        screen.blit(
            level,
            level.get_rect(topright=(self.board_left + BOARD_WIDTH, 85)),
        )

    def draw_overlay(
        self,
        screen: pygame.Surface,
        title: str,
        message: str,
    ) -> None:
        """Display a translucent message over the board."""
        overlay = pygame.Surface(
            (BOARD_WIDTH, BOARD_HEIGHT),
            pygame.SRCALPHA,
        )

        overlay.fill((0, 0, 0, 190))

        screen.blit(
            overlay,
            (self.board_left, BOARD_TOP),
        )

        title_surface = self.title_font.render(title, True, NEON_GREEN)

        message_surface = self.text_font.render(message, True, WHITE)

        center_y = BOARD_TOP + BOARD_HEIGHT // 2

        screen.blit(
            title_surface,
            title_surface.get_rect(center=(SCREEN_WIDTH // 2, center_y - 30)),
        )

        screen.blit(
            message_surface,
            message_surface.get_rect(center=(SCREEN_WIDTH // 2, center_y + 30)),
        )

    def render(self, screen: pygame.Surface) -> None:
        """Render the complete game screen."""
        self.draw_board(screen)
        self.draw_hud(screen)

        if self.logic.food is not None:
            self.draw_cell(
                screen,
                self.logic.food,
                FOOD_COLOUR,
            )

        for index, position in enumerate(self.logic.snake):
            colour = HEAD_COLOUR if index == 0 else SNAKE_COLOUR

            self.draw_cell(screen, position, colour)

        instructions = self.small_font.render(
            "ARROWS / WASD: Move | P: Pause | R: Restart | ESC: Menu",
            True,
            GREY,
        )

        screen.blit(
            instructions,
            instructions.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 35)),
        )

        if self.logic.won:
            self.draw_overlay(
                screen,
                "YOU WIN!",
                f"Final score: {self.logic.score} | R: Restart",
            )

        elif self.logic.game_over:
            self.draw_overlay(
                screen,
                "GAME OVER",
                f"Final score: {self.logic.score} | R: Restart",
            )

        elif self.logic.paused:
            self.draw_overlay(
                screen,
                "PAUSED",
                "Press P to resume",
            )

        elif not self.started:
            self.draw_overlay(
                screen,
                "READY?",
                "Press a movement key to start",
            )
