"""Логика игры Прогрессия."""
from random import randrange

from brain_games.random_numbers import random_numbers

recommend_len_max = 10
recommend_len_min = 5
rand_len = randrange(recommend_len_min, recommend_len_max)


def progression():
    """Вычисление примера и результата."""
    numbers = random_numbers()
    expression = []
    fist_number = numbers[0]
    progression_step = randrange(2, 5)
    while len(expression) <= rand_len:
        expression.append(fist_number)
        fist_number += progression_step
    answer = expression[randrange(0, rand_len)]
    expression[expression.index(answer)] = '..'
    return ' '.join(map(str, expression)), answer
