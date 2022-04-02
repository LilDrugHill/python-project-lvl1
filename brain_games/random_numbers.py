"""Random numbers generaitor."""
import random


def random_numbers():
    """Функция создания рандомных чисел."""
    sign = random.randrange(1, 3)
    number1 = random.randrange(1, 100)
    number2 = random.randrange(1, 100)
    numbers = [number1, number2, sign]
    return numbers
