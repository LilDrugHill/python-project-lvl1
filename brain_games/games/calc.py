"""Calc logic."""
from random import choice, randrange

INTRO = 'What is the result of the expression?'
MAX_POSIBLE_VALUE = 100


def expression_and_answer_generating():
    """Вычисление примера и результата for clac."""
    first_number = randrange(1, 100)
    second_number = randrange(1, 100)
    sign = choice(['+', '-', '*'])
    if sign == '+':
        answer = first_number + second_number
        expression = f'{first_number} + {second_number}'
    elif sign == '-':
        answer = first_number - second_number
        expression = f'{first_number} - {second_number}'
    elif sign == '*':
        answer = first_number * second_number
        expression = f'{first_number} * {second_number}'
    return expression, answer


if __name__ == '__main__':
    expression_and_answer_generating()
