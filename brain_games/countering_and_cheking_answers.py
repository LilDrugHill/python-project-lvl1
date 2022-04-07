"""Основание игры."""

from brain_games.scripts.brain_games import main

name = main()
while_breaker = -10
so_far_str = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def counter_game(function):
    """Choosing intriductory word depeding on function and count corrent answers.

    Args:
        function: the main constant determining the course of the game.
    """
    introductory_word = {
        'even': 'Answer "yes" if the number is even, otherwise answer "no".',
        'calc': 'What is the result of the expression?',
        'gcd': 'Find the greatest common divisor of given numbers.',
        'progression': 'What number is missing in the progression?',
        'prime': so_far_str,
    }
    print(introductory_word.get(function))
    right_answers = 0
    right_answers = answer_check(function())
    while right_answers in range(0, 3):
        right_answers += answer_check(function())
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
