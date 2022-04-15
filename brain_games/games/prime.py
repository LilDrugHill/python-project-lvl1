"""Prime logic."""
from random import randrange

from sympy import isprime

MAX_POSIBLE_VALUE = 100
INTRO_WORD = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def expression_and_answer_generating():
    """Вычисление примера и результата for prime."""
    number = randrange(1, MAX_POSIBLE_VALUE)
    expression = f'{number}'
    return expression, 'yes' if isprime(number) else 'no'


if __name__ == '__main__':
    expression_and_answer_generating()
