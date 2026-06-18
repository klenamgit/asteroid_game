# Asteroid Game

A pygame-based asteroid arcade game built with Python.

## Requirements

- Python 3.13+
- pygame 2.6.1

## Install

```bash
uv sync
```

## Run

```bash
uv run python main.py
```

## Controls

| Key | Action |
| --- | --- |
| `A` | Rotate left |
| `D` | Rotate right |
| `W` | Thrust forward |
| `S` | Move backward |
| `Space` | Fire a shot |

## Gameplay

The player starts in the center of a `1280x720` window. Asteroids spawn from the screen edges and move inward. Shots split asteroids into smaller pieces until they reach the minimum radius, at which point they are destroyed. The game ends when an asteroid collides with the player.

## Project Structure

- `main.py` - Initializes pygame, creates sprite groups, runs the game loop, and handles collisions.
- `player.py` - Player movement, rotation, and shooting logic.
- `asteroid.py` - Asteroid drawing, movement, and splitting behavior.
- `asteroidfield.py` - Periodic asteroid spawning from random screen edges.
- `shot.py` - Projectile movement and rendering.
- `circleshape.py` - Base circle-shaped sprite with position, velocity, radius, and collision helper.
- `constants.py` - Game dimensions, speeds, sizes, and timing values.
- `logger.py` - Writes periodic state snapshots to `game_state.jsonl` and collision events to `game_events.jsonl`.

## Logs

Running the game creates two local JSONL log files:

- `game_state.jsonl` - Snapshot of sprite groups and positions for the first 16 seconds.
- `game_events.jsonl` - Event records for player hits, asteroid shots, splits, and destroyed asteroids.

These log files are ignored by git.
