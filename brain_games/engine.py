"""Основание игры."""
import prompt
from brain_games.cli import welcome_user
from brain_games.scripts.brain_games import main

NUMBER_OF_ROUNDS = 3
LOOSE_MASSAGE = "\"{0}\" is wrong answer ;(.\
Correct answer was \"{1}\".\nLet's try again, {2}!"


def game_starting(game):
    """Import game and start scoring.

    Args:
        game: the main constant determining the course of the game.
    """
    main()
    name = prompt.string('May I have your name? ')
    welcome_user(name)
    print(game.INTRO)
    for _ in range(NUMBER_OF_ROUNDS):
        (expression, right_answer) = (
            game.expression_and_answer_generating()
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
