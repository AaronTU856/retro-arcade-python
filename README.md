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

## Planned Games

- Snake
- Pong
- Breakout
- Space Invaders-style shooter
- Falling block puzzle

## Planned Features

- Arcade game selection menu
- Keyboard controls
- Player profiles
- High-score leaderboard
- SQLite database
- Retro graphics and sound effects
- Difficulty settings
- Achievement system
- Game statistics
- Automated testing
- Continuous integration

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application development |
| Pygame | Game engine and graphics |
| SQLite | Planned data persistence |
| Pytest | Automated testing |
| Ruff | Linting and formatting |
| Pre-commit | Code quality checks |
| GitHub Actions | Continuous integration |

## Current Status

**Version: 0.1.0 — Initial Development**

The project structure and development environment are established.
Game development is planned for the next development phase.

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

MIT License — once the licence file has been configured.
