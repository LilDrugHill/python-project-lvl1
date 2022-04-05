#!/usr/bin/env python
"""STEP 7."""

from brain_games.engine import counter_game

game_id = 3


def brain_gcd():
    """Функция запуска игры. Тут в функцию поступает game_id."""
    counter_game(game_id)  # <-


if __name__ == '__main__':
    brain_gcd()
