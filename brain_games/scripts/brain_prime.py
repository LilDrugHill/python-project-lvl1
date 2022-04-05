#!/usr/bin/env python
"""STEP 9."""

from random import randrange

from brain_games.engine import counter_game

game_id = 5


def brain_prime():
    """Функция запуска игры. Тут в функцию поступает game_id."""
    counter_game(game_id)  # <-


def prime():
    """Вычисление примера и результата."""
    number = randrange(1, 100)
    index = 100
    divisor_count = 0
    while index > 0:
        if number % index == 0:
            divisor_count += 1
        index -= 1
    if divisor_count == 2:
        return f'{number}', 'yes'
    return f'{number}', 'no'


if __name__ == '__main__':
    brain_prime()
