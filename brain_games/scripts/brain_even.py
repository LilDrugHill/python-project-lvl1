#!/usr/bin/env python
"""STEP 5."""
from brain_games import engine
from brain_games.games import even


def brain_even():
    """Функция запуска игры."""
    engine.start(even)


if __name__ == '__main__':
    brain_even()
