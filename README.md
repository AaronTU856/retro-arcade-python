# Retro Arcade Python

A modular retro gaming arcade built with Python and Pygame.

Retro Arcade is a personal portfolio and learning project designed
to explore game development, object-oriented programming, software
architecture, algorithms and data persistence.

## Project Goals

- Develop a collection of classic retro-style games.
- Create a shared arcade interface.
- Implement reusable game components.
- Store player scores and gaming statistics.
- Apply professional software development practices.

## Games

| Game  | Status |
|---    |---     |
| Snake | Implemented |
| Pong  | Planned |
| Breakout | Planned |
| Space Invaders-style shooter | Planned |
| Falling block puzzle | Planned |

## Implemented Features

- Modular arcade engine
- Scene-based architecture
- Interactive main menu
- Keyboard navigation
- Playable Snake game
- Random food generation
- Collision detection
- Score tracking
- Progressive difficulty
- Pause and restart functionality
- Automated unit testing
- GitHub Actions continuous integration

## Current Status

**Version: 0.2.0 — First Playable Game**

The core arcade engine and the first playable game,
Snake, have been implemented.

## Screenshots

### Main Menu

![Main Menu](screenshots/main-menu.png)

### Snake Gameplay

![Snake Gameplay](screenshots/snake-gameplay.png)

### Game Over

![Game Over](screenshots/snake-game-over.png)

## Running the Application

```bash
retro-arcade
```

## Snake Controls

| Key | Action |
|---|---|
| Arrow keys / WASD | Move |
| P | Pause / Resume |
| R | Restart |
| ESC | Return to menu |


## Installation

Clone the repository and navigate to the project directory.

Create a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the application and development dependencies:

```bash
pip install -e ".[dev]"
```

## Development

Run linting:

```bash
ruff check .
```

Run formatting:

```bash
ruff format .
```

Run tests:

```bash
pytest
```

## Licence

This project is licensed under the MIT License.
See the [LICENSE](LICENSE) file for details.
