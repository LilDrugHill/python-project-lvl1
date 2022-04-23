"""Gcd logic."""
from math import gcd
from random import randrange

MAX_POSSIBLE_VALUE = 100
INTRO = 'Find the greatest common divisor of given numbers.'


def generate_expression_and_answer():
    """Вычисление примера и результата."""
    first_number = randrange(1, MAX_POSSIBLE_VALUE)
    second_number = randrange(1, MAX_POSSIBLE_VALUE)
    answer = gcd(first_number, second_number)
    return f'{first_number} {second_number}', answer


if __name__ == '__main__':
    generate_expression_and_answer()
