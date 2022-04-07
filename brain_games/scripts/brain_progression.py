#!/usr/bin/env python
"""STEP 8."""
import brain_games.countering_and_cheking_answers
from brain_games.games_logic import progression


def brain_progression():
    """Функция запуска игры. Тут в функцию поступает game_id."""
    brain_games.countering_and_cheking_answers.counter_game(progression)  # <-


if __name__ == '__main__':
    brain_progression()
