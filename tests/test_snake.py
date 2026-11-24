"""Automated tests for Snake game logic."""

from retro_arcade.games.snake.config import (
    GRID_COLUMNS,
    GRID_ROWS,
    INITIAL_LENGTH,
    INITIAL_SPEED,
    MAX_SPEED,
    POINTS_PER_FOOD,
)
from retro_arcade.games.snake.logic import (
    LEFT,
    RIGHT,
    UP,
    SnakeLogic,
)


def test_initial_state():
    game = SnakeLogic()

    assert len(game.snake) == INITIAL_LENGTH
    assert game.score == 0
    assert game.direction == RIGHT
    assert game.game_over is False
    assert game.paused is False


def test_snake_movement():
    game = SnakeLogic()

    x, y = game.head
    game.food = (0, 0)
    game.move()

    assert game.head == (x + 1, y)
    assert len(game.snake) == INITIAL_LENGTH


def test_change_direction():
    game = SnakeLogic()

    game.change_direction(UP)
    game.move()

    assert game.direction == UP


def test_prevent_reverse_direction():
    game = SnakeLogic()

    game.change_direction(LEFT)
    game.move()

    assert game.direction == RIGHT


def test_food_not_inside_snake():
    game = SnakeLogic()

    for _ in range(100):
        food = game.generate_food()

        assert food not in game.snake


def test_food_within_board():
    game = SnakeLogic()

    x, y = game.food

    assert 0 <= x < GRID_COLUMNS
    assert 0 <= y < GRID_ROWS


def test_food_consumption():
    game = SnakeLogic()

    x, y = game.head
    game.food = (x + 1, y)

    game.move()

    assert game.score == POINTS_PER_FOOD
    assert len(game.snake) == INITIAL_LENGTH + 1


def test_wall_collision():
    game = SnakeLogic()

    game.snake = [(GRID_COLUMNS - 1, 5)]

    game.move()

    assert game.game_over is True


def test_self_collision():
    game = SnakeLogic()

    game.snake = [
        (5, 5),
        (5, 6),
        (6, 6),
        (6, 5),
        (6, 4),
    ]

    game.food = (0, 0)
    game.move()

    assert game.game_over is True


def test_move_into_vacating_tail():
    game = SnakeLogic()

    game.snake = [
        (5, 5),
        (5, 6),
        (6, 6),
        (6, 5),
    ]

    game.food = (0, 0)
    game.move()

    assert game.game_over is False
    assert game.head == (6, 5)


def test_pause():
    game = SnakeLogic()

    original_position = game.head

    game.toggle_pause()
    game.move()

    assert game.paused is True
    assert game.head == original_position


def test_resume():
    game = SnakeLogic()

    game.toggle_pause()
    game.toggle_pause()

    assert game.paused is False


def test_level_increase():
    game = SnakeLogic()

    game.score = 50

    assert game.level == 2


def test_speed_increase():
    game = SnakeLogic()

    game.score = 50

    assert game.speed == INITIAL_SPEED + 1


def test_maximum_speed():
    game = SnakeLogic()

    game.score = 10000

    assert game.speed == MAX_SPEED


def test_reset():
    game = SnakeLogic()

    game.score = 100
    game.game_over = True
    game.paused = True

    game.reset()

    assert game.score == 0
    assert game.game_over is False
    assert game.paused is False
    assert len(game.snake) == INITIAL_LENGTH


def test_no_movement_after_game_over():
    game = SnakeLogic()

    original_position = game.head
    game.game_over = True

    game.move()

    assert game.head == original_position


def test_full_board_victory():
    game = SnakeLogic()

    game.snake = [
        (x, y)
        for y in range(GRID_ROWS)
        for x in range(GRID_COLUMNS)
        if (x, y) != (1, 0)
    ]

    game.food = (1, 0)
    game.move()

    assert game.won is True
    assert game.game_over is True
    assert game.food is None
