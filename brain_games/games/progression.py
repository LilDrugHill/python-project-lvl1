"""Progression logic."""
from random import randrange

RECOMMEND_LEN_MAX = 10
RECOMMEND_LEN_MIN = 5
rand_len = randrange(RECOMMEND_LEN_MIN, RECOMMEND_LEN_MAX)
INTRO_WORD = 'What number is missing in the progression?'


def expression_and_answer_generating():
    """Вычисление примера и результата for progression."""
    expression = []
    first_number = randrange(1, 100)
    progression_step = randrange(2, 5)
    while len(expression) <= rand_len:
        expression.append(first_number)
        first_number += progression_step
    answer = expression[randrange(0, rand_len)]
    expression[expression.index(answer)] = '..'
    return ' '.join(map(str, expression)), answer


if __name__ == '__main__':
    expression_and_answer_generating()
