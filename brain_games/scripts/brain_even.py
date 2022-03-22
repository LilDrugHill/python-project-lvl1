#!/usr/bin/env python
"""STEP 5."""

from brain_games.cli import welcome_user

name = welcome_user()


def main():
    """Функция сравнивает ответ и оотсылает на след. ф-цию при верном ответе."""
    print('Answer "yes" if the number is even, otherwise answer "no".')
    print('Question: 15')
    answer1 = input()
    if answer1 == 'no':
        print('Your answer: no\nCorrect!')
        main_step2()
    else:
        print(f"'{answer1}' is wrong answer ;(. Correct answer was 'no'.")
        print(f"Let's try again, {name}!")


def main_step2():
    """Функция сравнивает ответ и оотсылает на след. ф-цию при верном ответе."""
    print('Question: 6')
    answer2 = input()
    if answer2 == 'yes':
        print('Your answer: yes\nCorrect!')
        main_step3()
    else:
        print(f"'{answer2}' is wrong answer ;(. Correct answer was 'yes'.")
        print(f"Let's try again, {name}!")


def main_step3():
    """Функция сравнивает ответ и оотсылает на след. ф-цию при верном ответе."""
    print('Question: 7')
    answer3 = input()
    if answer3 == 'no':
        print('Your answer: no\nCorrect!')
        print(f'Congratulations, {name}')
    else:
        print(f"'{answer3}' is wrong answer ;(. Correct answer was 'no'.")
        print(f"Let's try again, {name}!")


if __name__ == '__main__':
    main()
