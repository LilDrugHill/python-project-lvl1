#!/usr/bin/env python
"""STEP 5."""
import brain_games.engine
import brain_games.games.even


def brain_even():
    """Функция запуска игры."""
    brain_games.engine.countering_games_score(brain_games.games.even)  # <-


if __name__ == '__main__':
    brain_even()
