#!/usr/bin/env python
"""STEP 9."""

from brain_games.engine import counter_game

game_id = 5


def brain_prime():
    """Функция запуска игры. Тут в функцию поступает game_id."""
    counter_game(game_id)  # <-


if __name__ == '__main__':
    brain_prime()
