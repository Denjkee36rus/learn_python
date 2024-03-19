import math
import random

n: int = int(input())
GUESS: int = random.randint(1, n + 1)


def get_possible_number_of_attempt(guess: int) -> int:
    """
    Находит, логорифм числа основание 2, для нахождения количества попыток.
    """
    return math.ceil(math.log(guess, 2))


def game(rand_num: int) -> None:
    attempt: int = get_possible_number_of_attempt(rand_num)
    print('Добро пожаловать в числовую угадайку')
    while attempt > 0:
        user_number: int = int(input('Ваш ответ: '))

        if user_number == rand_num:
            print("Победа!!! Вы угадали!")
            break

        if user_number < rand_num:
            print('Загаданное число больше')
        elif user_number > rand_num:
            print('Загаданное число меньше')
        attempt -= 1
    else:
        print(f'Вы проиграли, загаданное число {rand_num}')


game(GUESS)
