#!/usr/bin/env python
"""STEP 7."""

from random import randrange

from brain_games.engine import counter_game

game_id = 3


def brain_gcd():
    """Функция запуска игры. Тут в функцию поступает game_id."""
    counter_game(game_id)  # <-


def gcd():
    """Вычисление примера и результата."""
    first_number = randrange(1, 100)
    sec_number = randrange(1, 100)
    index = 100
    while index:
        if first_number % index == 0:
            if sec_number % index == 0:
                return f'{first_number} {sec_number}', index
        index -= 1


if __name__ == '__main__':
    brain_gcd()
