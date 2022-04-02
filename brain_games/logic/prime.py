"""Prime logic."""
from brain_games.random_numbers import random_numbers


def prime():
    """Вычисление примера и результата."""
    numbers = random_numbers()
    index = 100
    divisor_count = 0
    while index > 0:
        if numbers[0] % index == 0:
            divisor_count += 1
        index -= 1
    if divisor_count == 2:
        return f'{numbers[0]}', 'yes'
    return f'{numbers[0]}', 'no'
