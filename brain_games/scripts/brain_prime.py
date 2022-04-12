#!/usr/bin/env python
"""STEP 9."""
import brain_games.engine
import brain_games.games.prime


def brain_prime():
    """Функция запуска игры."""
    brain_games.engine.countering_games_score(brain_games.games.prime)


if __name__ == '__main__':
    brain_prime()
