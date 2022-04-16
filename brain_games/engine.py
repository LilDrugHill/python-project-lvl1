"""Основание игры."""
from brain_games.scripts.brain_games import main

NUMBER_OF_ROUNDS = 3
LOSE_MASSAGE = "\"{0}\" is wrong answer ;(.\
Correct answer was \"{1}\".\nLet's try again, {2}!"


def game_starting(game):
    """Import game and start scoring.

    Args:
        game: the main constant determining the course of the game.
    """
    name = main()
    print(game.INTRO)
    for _ in range(NUMBER_OF_ROUNDS):
        (expression, right_answer) = (
            game.expression_and_answer_generating()
        )
        print(f'Question: {expression}')
        players_answer = str(input())
        if str(right_answer) == players_answer:
            print('Correct!')
        else:
            print(LOSE_MASSAGE.format(players_answer, right_answer, name))
            break
    else:
        print(f'Congratulations, {name}!')
