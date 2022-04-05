#!/usr/bin/env python
"""STEP 8."""

from random import randrange

import brain_games.engine

game_id = 4
recommend_len_max = 10
recommend_len_min = 5
rand_len = randrange(recommend_len_min, recommend_len_max)


def brain_progression():
    """Функция запуска игры. Тут в функцию поступает game_id."""
    brain_games.engine.counter_game(game_id)  # <-


def progression():
    """Вычисление примера и результата."""
    expression = []
    fist_number = randrange(1, 100)
    progression_step = randrange(2, 5)
    while len(expression) <= rand_len:
        expression.append(fist_number)
        fist_number += progression_step
    answer = expression[randrange(0, rand_len)]
    expression[expression.index(answer)] = '..'
    return ' '.join(map(str, expression)), answer


if __name__ == '__main__':
    brain_progression()
