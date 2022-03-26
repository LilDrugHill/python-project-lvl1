"""Рандомайзер ответа и примера."""

from os import nice
import random
from re import I


def random_number():
    """Функция создания рандомных чисел."""
    sign = random.randrange(1, 3)
    number1 = random.randrange(1, 100)
    number2 = random.randrange(1, 100)
    numbers = [number1, number2, sign]
    return numbers


def choosen_expression_result(way, numbers):
    """Функция производства примера и ответа в зависимости от way."""
    if way == 1:
        expression = numbers[0]
        if numbers[0] % 2 == 0:
            result = 'yes'
        else:
            result = 'no'
    elif way == 2:
        if numbers[2] == 1:
            result = numbers[0] + numbers[1]
            expression = f'{numbers[0]} + {numbers[1]}'
        elif numbers[2] == 2:
            result = numbers[0] - numbers[1]
            expression = f'{numbers[0]} - {numbers[1]}'
        elif numbers[2] == 3:
            result = numbers[0] * numbers[1]
            expression = f'{numbers[0]} * {numbers[1]}'
    elif way == 3:
        i = 100
        result = 0
        expression = f'{numbers[0]} {numbers[1]}'
        while i > 0 and result == 0:
            if numbers[0] % i == 0 and numbers[1] % i == 0:
                result = i  
            i -= 1
    elif way == 4:
        secret_number = random.randrange(0, 9)
        len_progression = random.randrange(4, 15) 
        progression = []
        i = numbers[0]
        while len(progression) < len_progression:
            progression.append(i)
            i += numbers[1]  
        result = progression[secret_number]
        expression = progression
        expression[secret_number] = '..'
    elif way == 5:
        i = 100
        divisor_count = 0
        expression = f'{numbers[0]}'
        while i > 0:
            if numbers[0] % i == 0:
                divisor_count += 1
            i -= 1
        if divisor_count == 2:
            result = 'yes'
        else:
            result = 'no'     
    exrossion_result = [expression, result]
    return exrossion_result
