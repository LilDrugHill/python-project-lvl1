#!/usr/bin/env python
"""STEP 6."""
import brain_games.engine
import brain_games.games.calc


def brain_calc():
    """Функция запуска игры."""
    brain_games.engine.countering_games_score(brain_games.games.calc)


if __name__ == '__main__':
    brain_calc()
