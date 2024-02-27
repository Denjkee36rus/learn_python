import random

START: int = 1
END: int = 100
ATTEMPT: int = 5

# TODO:  1. Бот загадает число в диапазоне от START до END
# Загаданное число
GUESS: int = random.randint(START, END)


# TODO: 3. Реализацию нужно декомпозировать
def check_num(num: int) -> bool:
    """
    Проверяет, входит ли переданное число в диапазон от START до END.

    :param num: Число для проверки.
    """
    return num in range(START, END + 1)


def game() -> str:
    """
    Реализация игры "Угадай число".
    """
    attempt: int = 0
    # TODO: 2. Дается ATTEMPT попыток на угадывания
    while attempt < ATTEMPT:
        user_num: int = int(input())

        # CTRL + Q
        if check_num(user_num):

            if user_num == GUESS:
                return 'Вы угадали!'
            elif user_num < GUESS:
                print('Загаданное число больше')
            elif user_num > GUESS:
                print('Загаданное число меньше')
            attempt += 1

        else:  # Если ответ пользователя не входит в диапазон от START до END
            print(f'Укажите число в диапазоне от {START} до {END}')
            attempt += 1

    return f'Вы проиграли, загаданное число {GUESS}'


print(game())
