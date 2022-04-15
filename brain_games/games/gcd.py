"""Gcd logic."""
from math import gcd
from random import randrange

MAX_POSIBLE_VALUE = 100
INTRO_WORD = 'Find the greatest common divisor of given numbers.'


def expression_and_answer_generating():
    """Вычисление примера и результата."""
    first_number = randrange(1, MAX_POSIBLE_VALUE)
    second_number = randrange(1, MAX_POSIBLE_VALUE)
    answer = gcd(first_number, second_number)
    return f'{first_number} {second_number}', answer


if __name__ == '__main__':
    expression_and_answer_generating()
