#!/usr/bin/env python
"""STEP 5."""
import brain_games.countering_and_cheking_answers
from brain_games.games_logic import even


def brain_even():
    """Функция запуска игры. Тут в функцию поступает game_id."""
    brain_games.countering_and_cheking_answers.counter_game(even)  # <-


if __name__ == '__main__':
    brain_even()
