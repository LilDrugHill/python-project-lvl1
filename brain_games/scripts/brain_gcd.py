#!/usr/bin/env python
"""STEP 7."""
import brain_games.engine
import brain_games.games.gcd 


def brain_gcd():
    """Функция запуска игры."""
    brain_games.engine.countering_games_score(brain_games.games.gcd)  # <-


if __name__ == '__main__':
    brain_gcd()
