"""Calc game logic."""
from random import randrange


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
