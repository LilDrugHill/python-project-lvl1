"""Основание игры."""
import brain_games.scripts.brain_calc
import brain_games.scripts.brain_even
import brain_games.scripts.brain_games
import brain_games.scripts.brain_gcd
import brain_games.scripts.brain_prime
import brain_games.scripts.brain_progression

name = brain_games.scripts.brain_games.main()
while_breaker = -10


def counter_game(game_id):
    """Choosing intriductory word depeding on game_id and count corrent answers.

    Args:
        game_id: the main constant determining the course of the game.
    """
    introductory_word = {
        1: 'Answer "yes" if the number is even, otherwise answer "no".',
        2: 'What is the result of the expression?',
        3: 'Find the greatest common divisor of given numbers.',
        4: 'What number is missing in the progression?',
        5: 'Answer "yes" if given number is prime. Otherwise answer "no".',
    }
    expression_result = {
        1: brain_games.scripts.brain_even.even(),
        2: brain_games.scripts.brain_calc.calc(),
        3: brain_games.scripts.brain_gcd.gcd(),
        4: brain_games.scripts.brain_progression.progression(),
        5: brain_games.scripts.brain_prime.prime(),
    }
    print(introductory_word.get(game_id))
    right_answers = 0
    right_answers = answer_check(expression_result.get(game_id))
    while right_answers in range(0, 3):
        expression_result = {
            1: brain_games.scripts.brain_even.even(),
            2: brain_games.scripts.brain_calc.calc(),
            3: brain_games.scripts.brain_gcd.gcd(),
            4: brain_games.scripts.brain_progression.progression(),
            5: brain_games.scripts.brain_prime.prime(),
        }
        right_answers += answer_check(expression_result.get(game_id))
    if right_answers == 3:
        print(f'Congratulations, {name}!')


def answer_check(exp_answer):
    """Проверка ответа и вывод слов поддержки.

    Args:
        exp_answer: tuple containing expression and answer.
    """
    print(f'Question: {exp_answer[0]}')
    answer = input()
    if answer == str(exp_answer[1]):
        print('Correct!')
        right_answers = 1
        return right_answers
    print(
        f"'{answer}' is wrong answer ;(. Correct answer was '{exp_answer[1]}'.",
    )
    print(f"Let's try again, {name}!")
    right_answers = while_breaker
    return right_answers
