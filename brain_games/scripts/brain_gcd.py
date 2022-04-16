#!/usr/bin/env python
"""STEP 7."""
from brain_games import engine
from brain_games.games import gcd


def brain_gcd():
    """Функция запуска игры."""
    engine.game_starting(gcd)


if __name__ == '__main__':
    brain_gcd()
