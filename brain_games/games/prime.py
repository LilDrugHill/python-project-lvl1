"""Prime logic."""
import math
from random import randrange

MAX_POSSIBLE_VALUE = 100
INTRO = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_expression_and_answer():
    """Вычисление примера и результата for prime."""
    number = randrange(1, MAX_POSSIBLE_VALUE)
    expression = f'{number}'
    return expression, 'no' if is_prime(number) else 'yes'


def is_prime(number):
    """Is the number is prime.

    Args:
        number: given number.
    """
    index = 2
    while index <= math.sqrt(number):
        if not number % index:
            return 1
        index += 1


if __name__ == '__main__':
    generate_expression_and_answer()
