START: int = 1
END: int = 100
LIFE: int = 7


def game_with_bot():
    low, high = START, END

    print(f'Загадайте число от {START} до {END}'
          '\nЯ буду угадывать число Вы должны ответить '
          '"больше", "меньше" или "угадал" если я угадал Ваше число')

    attempt: int = 0
    while attempt < LIFE:
        attempt += 1

        guess: int = (low + high) // 2
        print(f'Бот: мой вариант - {guess}')
        user_ans: str = input('Бот: Это Ваше число?: ').lower()

        if user_ans == 'угадал':
            return f'Бот: Бот угадал Ваше число за {attempt} попыток'

        if user_ans == 'больше':
            low = guess - 1
        elif user_ans == 'меньше':
            high = guess + 1
        else:
            print('Пожалуйста, введите "больше", "меньше" или "угадал"')
    return 'Бот: Бот проиграл не смог угадать Ваше число'


if __name__ == '__main__':
    print(game_with_bot())
