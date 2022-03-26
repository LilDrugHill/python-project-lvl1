#!/usr/bin/env python
"""STEP 5."""

from brain_games.check_count import counter_game
from brain_games.expr_result import random_numbers
from brain_games.scripts.brain_games import main


def brain_even():
    """Функция запуска игры. Тут в функцию поступает way."""
    name = main()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    numbers = random_numbers()
    expression = numbers[0]
    if numbers[0] % 2 == 0:
        result = 'yes'
    else:
        result = 'no'
    expression_result = [expression, result]
    counter_game(expression_result, name)
    

if __name__ == '__main__':
    brain_even()
