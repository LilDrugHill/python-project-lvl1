"""module for main function."""

import prompt


def welcome_user():
    """Испозьет функцию из пакета prompt."""
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
