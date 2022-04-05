"""Even or not logic."""
from random import randrange


def even():
    """Вычисление примера и результата."""
    number = randrange(1, 100)
    if number % 2 == 0:
        return number, 'yes'
    return number, 'no'
