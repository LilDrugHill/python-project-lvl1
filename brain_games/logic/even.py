"""Even or not logic."""
from brain_games.random_numbers import random_numbers


def even():
    """Вычисление примера и результата."""
    numbers = random_numbers()
    if numbers[0] % 2 == 0:
        return numbers[0], 'yes'
    return numbers[0], 'no'
