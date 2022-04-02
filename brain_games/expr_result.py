"""Choose logic."""
from brain_games.logic.calc import calc
from brain_games.logic.even import even
from brain_games.logic.gcd import gcd
from brain_games.logic.prime import prime
from brain_games.logic.progression import progression


def choosen_expression_result(way):
    """Choosing func depeding on way.

    Args:
        way: the main constant determining the course of the game.
    """
    expression_result = {
        1: even(),
        2: calc(),
        3: gcd(),
        4: progression(),
        5: prime(),
    }
    return expression_result.get(way)
