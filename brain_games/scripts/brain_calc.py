#!/usr/bin/env python
"""STEP 6."""
from brain_games import engine
from brain_games.games import calc


def brain_calc():
    """Функция запуска игры."""
    engine.start(calc)


if __name__ == '__main__':
    brain_calc()
