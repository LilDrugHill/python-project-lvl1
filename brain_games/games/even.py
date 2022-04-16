"""Even logic."""
from random import randrange

INTRO = 'Answer "yes" if the number is even, otherwise answer "no".'
MAX_POSIBLE_VALUE = 100


def expression_and_answer_generating():
    """Вычисление примера и результата for even."""
    number = randrange(1, 100)
    if number % 2 == 0:
        return number, 'yes'
    return number, 'no'


if __name__ == '__main__':
    expression_and_answer_generating()
