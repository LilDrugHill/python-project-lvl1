"""Calc logic."""
from random import randrange

print('What is the result of the expression?')


def playing():
    """Вычисление примера и результата for clac."""
    first_number = randrange(1, 100)
    sec_number = randrange(1, 100)
    sign = randrange(1, 3)
    if sign == 1:
        answer = first_number + sec_number
        expression = f'{first_number} + {sec_number}'
    elif sign == 2:
        answer = first_number - sec_number
        expression = f'{first_number} - {sec_number}'
    elif sign == 3:
        answer = first_number * sec_number
        expression = f'{first_number} * {sec_number}'
    return expression, answer

if __name__ == '__main__':
    playing()
