#!/usr/bin/env python
"""STEP 3."""

from brain_games.cli import welcome_user


def main():
    """Функция приветсвия и создания имени."""
    print('Welcome to the Brain Games!')
    name = welcome_user()
    return name


if __name__ == '__main__':
    main()
