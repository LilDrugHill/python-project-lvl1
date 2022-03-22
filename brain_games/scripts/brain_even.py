#!/usr/bin/env python

from brain_games.cli import welcome_user

def brain_even_1_step():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    print('Question: 15')
    answer1 = input()
    if answer1 == 'no':
        print('Your answer: no/nCorrect!')

if __name__ == '__main__':
    brain_even_1_step()