"""Gcd game logic."""
from brain_games.random_numbers import random_numbers


def gcd():
    """Вычисление примера и результата."""
    numbers = random_numbers()
    index = 100
    while index:
        if numbers[0] % index == 0:
            if numbers[1] % index == 0:
                return f'{numbers[0]} {numbers[1]}', index
        index -= 1
