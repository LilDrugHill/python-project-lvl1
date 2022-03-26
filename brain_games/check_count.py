"""Основание игры."""

from brain_games.scripts.brain_games import main


def counter_game(expression_result, name):
    """Счетчик правильных ответов"""
    counter = answer_check(expression_result, name) 
    while 3 > counter > 0:          #Функция берет знавения из нижестоящий по логике функции
        counter += answer_check(expression_result, name)
    if counter == 3:
        print(f'Congratulations, {name}!')

def answer_check(expression_result, name):
    """Проверка ответа и вывод слов поддержки."""
    print(f'Question: {expression_result[0]}')
    answer = input()
    if answer == str(expression_result[1]):
        print('Correct!')
        counter =+ 1
        return counter  
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{expression_result[1]}'.")
        print(f"Let's try again, {name}!")
        counter =- 10
        return counter
        
        
    """ if way == 1:
        print('Answer "yes" if the number is even, otherwise answer "no".')
    elif way == 2:
        print('What is the result of the expression?')
    elif way == 3:
        print('Find the greatest common divisor of given numbers.')
    elif way == 4:
        print('What number is missing in the progression?')
    elif way == 5:
        print('Answer "yes" if given number is prime. Otherwise answer "no".')"""