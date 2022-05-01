"""Progression logic."""
from random import randrange

RECOMMEND_LEN_MAX = 10
RECOMMEND_LEN_MIN = 5
MAX_POSSIBLE_VALUE = 100
INTRO = 'What number is missing in the progression?'


def generate_expression_and_answer():
    """Вычисление примера и результата for progression."""
    expression = generate_progression()
    missing_num = randrange(0, len(expression))
    answer = expression[missing_num]
    expression[missing_num] = '..'
    return ' '.join(map(str, expression)), answer


def generate_progression():
    """Generate progression."""
    progression = []
    rand_len = randrange(RECOMMEND_LEN_MIN, RECOMMEND_LEN_MAX)
    first_number = randrange(1, MAX_POSSIBLE_VALUE)
    progression_step = randrange(2, 5)
    while len(progression) <= rand_len:
        progression.append(first_number)
        first_number += progression_step
    return progression


if __name__ == '__main__':
    generate_expression_and_answer()
