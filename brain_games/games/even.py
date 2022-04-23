"""Even logic."""
from random import randrange

INTRO = 'Answer "yes" if the number is even, otherwise answer "no".'
MAX_POSSIBLE_VALUE = 100


def generate_expression_and_answer():
    """Вычисление примера и результата for even."""
    number = randrange(1, MAX_POSSIBLE_VALUE)
    if number % 2 == 0:
        return number, 'yes'
    return number, 'no'


if __name__ == '__main__':
    generate_expression_and_answer()
