#!/usr/bin/env python
"""STEP 8."""
from brain_games import engine
from brain_games.games import progression


def brain_progression():
    """Функция запуска игры."""
    engine.game_starting(progression)


if __name__ == '__main__':
    brain_progression()
