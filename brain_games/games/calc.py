"""Calc logic."""
from random import choice, randrange

INTRO = 'What is the result of the expression?'
MAX_POSSIBLE_VALUE = 100


def generate_expression_and_answer():
    """Вычисление примера и результата for clac."""
    first_number = randrange(1, MAX_POSSIBLE_VALUE)
    second_number = randrange(1, MAX_POSSIBLE_VALUE)
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
    generate_expression_and_answer()
