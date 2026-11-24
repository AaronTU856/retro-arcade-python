"""Independent game logic for Snake."""

import random

from retro_arcade.games.snake.config import (
    GRID_COLUMNS,
    GRID_ROWS,
    INITIAL_LENGTH,
    INITIAL_SPEED,
    MAX_SPEED,
    POINTS_PER_FOOD,
    POINTS_PER_LEVEL,
)

Position = tuple[int, int]

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)


class SnakeLogic:
    """Manage the state and rules of the Snake game."""

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        """Restore the initial game state."""
        start_x = GRID_COLUMNS // 2
        start_y = GRID_ROWS // 2

        self.snake = [(start_x - index, start_y) for index in range(INITIAL_LENGTH)]

        self.direction = RIGHT
        self.next_direction = RIGHT

        self.score = 0
        self.game_over = False
        self.won = False
        self.paused = False

        self.food = self.generate_food()

    @property
    def head(self) -> Position:
        """Return the position of the snake's head."""
        return self.snake[0]

    @property
    def level(self) -> int:
        """Calculate the current difficulty level."""
        return 1 + self.score // POINTS_PER_LEVEL

    @property
    def speed(self) -> int:
        """Calculate movement speed."""
        return min(
            INITIAL_SPEED + self.level - 1,
            MAX_SPEED,
        )

    def generate_food(self) -> Position | None:
        """Generate food in an unoccupied grid cell."""
        occupied = set(self.snake)

        available = [
            (x, y)
            for x in range(GRID_COLUMNS)
            for y in range(GRID_ROWS)
            if (x, y) not in occupied
        ]

        if not available:
            return None

        return random.choice(available)

    def change_direction(self, direction: Position) -> None:
        """Change direction without allowing reversal."""
        if direction not in (UP, DOWN, LEFT, RIGHT):
            return

        opposite = (
            -self.direction[0],
            -self.direction[1],
        )

        if direction != opposite:
            self.next_direction = direction

    def toggle_pause(self) -> None:
        """Pause or resume the game."""
        if not self.game_over:
            self.paused = not self.paused

    def move(self) -> None:
        """Advance the snake by one grid cell."""
        if self.game_over or self.paused:
            return

        self.direction = self.next_direction

        head_x, head_y = self.head
        dx, dy = self.direction

        new_head = (head_x + dx, head_y + dy)

        if self.check_wall_collision(new_head):
            self.game_over = True
            return

        eating = new_head == self.food

        body = self.snake if eating else self.snake[:-1]

        if new_head in body:
            self.game_over = True
            return

        self.snake.insert(0, new_head)

        if eating:
            self.score += POINTS_PER_FOOD
            self.food = self.generate_food()

            if self.food is None:
                self.won = True
                self.game_over = True
        else:
            self.snake.pop()

    def check_wall_collision(self, position: Position) -> bool:
        """Determine whether a position is outside the board."""
        x, y = position

        return not (0 <= x < GRID_COLUMNS and 0 <= y < GRID_ROWS)
