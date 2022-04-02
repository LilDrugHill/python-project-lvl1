"""Calc game logic."""
from brain_games.random_numbers import random_numbers


def calc():
    """Вычисление примера и результата."""
    numbers = random_numbers()
    first_number = numbers[0]
    sec_number = numbers[1]
    if numbers[2] == 1:
        answer = numbers[0] + numbers[1]
        expression = f'{first_number} + {sec_number}'
    elif numbers[2] == 2:
        answer = numbers[0] - numbers[1]
        expression = f'{first_number} - {sec_number}'
    elif numbers[2] == 3:
        answer = numbers[0] * numbers[1]
        expression = f'{first_number} * {sec_number}'
    return expression, answer
