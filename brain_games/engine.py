"""Основание игры."""

import prompt

NUMBER_OF_ROUNDS = 3
LOOSE_MASSAGE = "\"{0}\" is wrong answer ;(.\
Correct answer was \"{1}\".\nLet's try again, {2}!"


def game_starting(game):
    """start.

    Args:
        game: the main constant determining the course of the game.
    """
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.INTRO)
    for _ in range(NUMBER_OF_ROUNDS):
        (expression, right_answer) = (
            game.generate_expression_and_answer()
        )
        print(f'Question: {expression}')
        players_answer = input()
        if str(right_answer) == players_answer:
            print('Correct!')
        else:
            print(LOOSE_MASSAGE.format(players_answer, right_answer, name))
            break
    else:
        print(f'Congratulations, {name}!')
