"""Основание игры."""

import prompt

NUMBER_OF_ROUNDS = 3


def start(game):
    """Import game and start scoring.

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
        player_answer = input()
        if str(right_answer) == player_answer:
            print('Correct!')
        else:
            print(f"\"{player_answer}\" is wrong answer ;(.Correct answer was \"{right_answer}\".\
            \nLet's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')
