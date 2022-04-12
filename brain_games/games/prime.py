"""Prime logic."""
from random import randrange

print('Answer "yes" if given number is prime. Otherwise answer "no".')


def playing():
    """Вычисление примера и результата for prime."""
    number = randrange(1, 100)
    index = 100
    divisor_count = 0
    while index > 0:
        if number % index == 0:
            divisor_count += 1
        index -= 1
    if divisor_count == 2:
        return f'{number}', 'yes'
    return f'{number}', 'no'


if __name__ == '__main__':
    playing()
