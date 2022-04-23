"""Progression logic."""
from random import randrange

RECOMMEND_LEN_MAX = 10
RECOMMEND_LEN_MIN = 5
MAX_POSSIBLE_VALUE = 100
INTRO = 'What number is missing in the progression?'


def generate_expression_and_answer():
    """Вычисление примера и результата for progression."""
    expression = []
    rand_len = randrange(RECOMMEND_LEN_MIN, RECOMMEND_LEN_MAX)
    first_number = randrange(1, MAX_POSSIBLE_VALUE)
    progression_step = randrange(2, 5)
    while len(expression) <= rand_len:
        expression.append(first_number)
        first_number += progression_step
    answer = expression[randrange(0, rand_len)]
    expression[expression.index(answer)] = '..'
    return ' '.join(map(str, expression)), answer


if __name__ == '__main__':
    generate_expression_and_answer()
