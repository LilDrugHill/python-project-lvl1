#!/usr/bin/env python
"""STEP 9."""
import brain_games.countering_and_cheking_answers
from brain_games.games_logic import prime


def brain_prime():
    """Функция запуска игры. Тут в функцию поступает game_id."""
    brain_games.countering_and_cheking_answers.counter_game(prime)  # <-


if __name__ == '__main__':
    brain_prime()
