"""Логика игры Прогрессия."""
from random import randrange

recommend_len_max = 10
recommend_len_min = 5
rand_len = randrange(recommend_len_min, recommend_len_max)


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
