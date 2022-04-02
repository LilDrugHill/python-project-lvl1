"""Основание игры."""

from brain_games.expr_result import choosen_expression_result
from brain_games.scripts.brain_games import main

name = main()


def counter_game(way):
    """Choosing intriductory word depeding on way and count corrent answers.

    Args:
        way: the main constant determining the course of the game.
    """
    introductory_word = {
        1: 'Answer "yes" if the number is even, otherwise answer "no".',
        2: 'What is the result of the expression?',
        3: 'Find the greatest common divisor of given numbers.',
        4: 'What number is missing in the progression?',
        5: 'Answer "yes" if given number is prime. Otherwise answer "no".',
    }
    print(introductory_word.get(way))
    right_answers = 0
    right_answers = answer_check(choosen_expression_result(way))
    while right_answers in range(0, 3):
        right_answers += answer_check(choosen_expression_result(way))
    if right_answers == 3:
        print(f'Congratulations, {name}!')


def answer_check(exp_answer):
    """Проверка ответа и вывод слов поддержки.

    Args:
        exp_answer: tuple containing expression and answer.
    """
    print(f'Question: {exp_answer[0]}')
    answer = input()
    if answer == str(exp_answer[1]):
        print('Correct!')
        right_answers = 1
        return right_answers
    print(
        f"'{answer}' is wrong answer ;(. Correct answer was '{exp_answer[1]}'.",
    )
    print(f"Let's try again, {name}!")
    right_answers = -10
    return right_answers
