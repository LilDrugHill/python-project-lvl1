#!/usr/bin/env python
"""STEP 9."""
from brain_games import engine
from brain_games.games import prime


def brain_prime():
    """Функция запуска игры."""
    engine.game_starting(prime)


if __name__ == '__main__':
    brain_prime()
