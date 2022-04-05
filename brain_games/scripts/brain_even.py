#!/usr/bin/env python
"""STEP 5."""

from random import randrange

import brain_games.engine

game_id = 1


def brain_even():
    """Функция запуска игры. Тут в функцию поступает game_id."""
    brain_games.engine.counter_game(game_id)  # <-


def even():
    """Вычисление примера и результата."""
    number = randrange(1, 100)
    if number % 2 == 0:
        return number, 'yes'
    return number, 'no'


if __name__ == '__main__':
    brain_even()
