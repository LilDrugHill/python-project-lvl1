"""Основание игры."""
from brain_games.games.calc import calc
from brain_games.games.even import even
from brain_games.games.gcd import gcd
from brain_games.games.prime import prime
from brain_games.games.progression import progression
from brain_games.scripts.brain_games import main

name = main()
while_breaker = -10


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
    expression_result = {
        1: even(),
        2: calc(),
        3: gcd(),
        4: progression(),
        5: prime(),
    }
    print(introductory_word.get(way))
    right_answers = 0
    right_answers = answer_check(expression_result.get(way))
    while right_answers in range(0, 3):
        expression_result = {
            1: even(),
            2: calc(),
            3: gcd(),
            4: progression(),
            5: prime(),
        }
        right_answers += answer_check(expression_result.get(way))
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
    right_answers = while_breaker
    return right_answers
