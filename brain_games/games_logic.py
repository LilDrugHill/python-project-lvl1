"""Games logic."""

from random import randrange

recommend_len_max = 10
recommend_len_min = 5
rand_len = randrange(recommend_len_min, recommend_len_max)


def calc():
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


def even():
    """Вычисление примера и результата for even."""
    number = randrange(1, 100)
    if number % 2 == 0:
        return number, 'yes'
    return number, 'no'


def gcd():
    """Вычисление примера и результата."""
    first_number = randrange(1, 100)
    sec_number = randrange(1, 100)
    index = 100
    while index:
        if first_number % index == 0:
            if sec_number % index == 0:
                return f'{first_number} {sec_number}', index
        index -= 1


def prime():
    """Вычисление примера и результата for prime."""
    number = randrange(1, 100)
    index = 100
    divisor_count = 0
    while index > 0:
        if number % index == 0:
            divisor_count += 1
        index -= 1
    if divisor_count == 2:
        return f'{number}', 'yes'
    return f'{number}', 'no'


def progression():
    """Вычисление примера и результата for progression."""
    expression = []
    fist_number = randrange(1, 100)
    progression_step = randrange(2, 5)
    while len(expression) <= rand_len:
        expression.append(fist_number)
        fist_number += progression_step
    answer = expression[randrange(0, rand_len)]
    expression[expression.index(answer)] = '..'
    return ' '.join(map(str, expression)), answer
