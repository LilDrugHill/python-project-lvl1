"""Основание игры."""
from brain_games.scripts.brain_games import main

TIMES_TO_WIN = 3
LOSE_MASSAGE = "\"{0}\" is wrong answer ;(. Correct answer was \"{1}\".\nLet's try again, {2}!"


def game_starting_and_score_counting(game_logic_module):
    """Import game_logic_module and start scoring.

    Args:
        game_logic_module: the main constant determining the course of the game.
    """
    name = main()
    print(game_logic_module.INTRO_WORD)
    for time in range(TIMES_TO_WIN):
        expression, right_answer = game_logic_module.expression_and_answer_generating()
        print(f'Question: {expression}')
        players_answer = str(input())
        if str(right_answer) == players_answer:
            print('Correct!')
        else:
            print(LOSE_MASSAGE.format(players_answer, right_answer, name))
            break
        if time == (list(range(TIMES_TO_WIN)))[-1]:
            print(f'Congratulations, {name}!')
