#!/usr/bin/env python
"""STEP 7."""
import brain_games.countering_and_cheking_answers
from brain_games.games_logic import gcd


def brain_gcd():
    """Функция запуска игры. Тут в функцию поступает game_id."""
    brain_games.countering_and_cheking_answers.counter_game(gcd)  # <-


if __name__ == '__main__':
    brain_gcd()
