"""Основание игры."""
from brain_games.scripts.brain_games import main

name = main()
while_breaker = -10
so_far_str = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def countering_games_score(module):
    """Choosing intriductory word depeding on module and count corrent answers.

    Args:
        module: the main constant determining the course of the game.
    """
    right_answers = 0
    right_answers = answer_checking(module.playing())
    while right_answers in range(0, 3):
        right_answers += answer_checking(module.playing())
    if right_answers == 3:
        print(f'Congratulations, {name}!')


def answer_checking(exp_answer):
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
