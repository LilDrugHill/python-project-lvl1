"""Prime logic."""
from random import randrange

MAX_POSIBLE_VALUE = 100
INTRO_WORD = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def expression_and_answer_generating():
    """Вычисление примера и результата for prime."""
    number = randrange(1, MAX_POSIBLE_VALUE)
    expression = f'{number}'
    return expression, is_prime(number)


def is_prime(number):
    """Is the number is prime.

    Args:
        number: given number.
    """
    number_of_divisors = 0
    index = number
    while index != 0:
        if number % index == 0:
            number_of_divisors += 1
        index -= 1
    if number_of_divisors <= 2:
        return 'yes'
    return 'no'


if __name__ == '__main__':
    expression_and_answer_generating()
