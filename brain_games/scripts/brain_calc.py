#!/usr/bin/env python
"""STEP 6."""
import brain_games.countering_and_cheking_answers
from brain_games.games_logic import calc


def brain_calc():
    """Функция запуска игры. Тут в функцию поступает game_id."""
    brain_games.countering_and_cheking_answers.counter_game(calc)


if __name__ == '__main__':
    brain_calc()
