#!/usr/bin/env python
"""STEP 8."""
import brain_games.engine
import brain_games.games.progression


def brain_progression():
    """Функция запуска игры."""
    brain_games.engine.countering_games_score(brain_games.games.progression)


if __name__ == '__main__':
    brain_progression()
