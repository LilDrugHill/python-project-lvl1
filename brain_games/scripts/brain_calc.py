#!/usr/bin/env python
"""STEP 6."""

from brain_games.engine import counter_game

game_id = 1


def brain_calc():
    """Функция запуска игры. Тут в функцию поступает game_id."""
    counter_game(game_id)  # <-


if __name__ == '__main__':
    brain_calc()
