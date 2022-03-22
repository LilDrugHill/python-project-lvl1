"""module for main function."""

import prompt


def welcome_user():
    """Испозьет функцию из пакета prompt. Function returns constant name."""
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name
