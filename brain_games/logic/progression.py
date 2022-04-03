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
    index = numbers[0]
    while len(expression) < rand_len:
        expression.append(index)
        index += numbers[1]
    answer = expression[randrange(0, rand_len)]
    expression[expression.index(answer)] = '..'
    return expression, answer
