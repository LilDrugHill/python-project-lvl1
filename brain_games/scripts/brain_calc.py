#!/usr/bin/env python
"""STEP 6."""

from random import randrange

import brain_games.engine 

game_id = 2


def brain_calc():
    """Функция запуска игры. Тут в функцию поступает game_id."""
    brain_games.engine.counter_game(game_id)  # <-


def calc():
    """Вычисление примера и результата."""
    first_number = randrange(1, 100)
    sec_number = randrange(1, 100)
    sign = randrange(1, 3)
    if sign == 1:
        answer = first_number + sec_number
        expression = f'{first_number} + {sec_number}'
    elif sign == 2:
        answer = first_number - sec_number
        expression = f'{first_number} - {sec_number}'
    elif sign == 3:
        answer = first_number * sec_number
        expression = f'{first_number} * {sec_number}'
    return expression, answer


if __name__ == '__main__':
    brain_calc()
