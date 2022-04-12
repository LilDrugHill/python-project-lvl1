"""Even logic."""
from random import randrange

print('Answer "yes" if the number is even, otherwise answer "no".')


def playing():
    """Вычисление примера и результата for even."""
    number = randrange(1, 100)
    if number % 2 == 0:
        return number, 'yes'
    return number, 'no'

if __name__ == '__main__':
    playing()
