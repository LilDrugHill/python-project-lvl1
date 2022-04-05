#!/usr/bin/env python
"""STEP 8."""

from brain_games.engine import counter_game

game_id = 5


def brain_progression():
    """Функция запуска игры. Тут в функцию поступает game_id."""
    counter_game(game_id)  # <-


if __name__ == '__main__':
    brain_progression()
