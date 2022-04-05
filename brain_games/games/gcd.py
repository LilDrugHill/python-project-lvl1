"""Gcd game logic."""
from random import randrange


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
