import random
from string import ascii_lowercase, ascii_uppercase, digits, punctuation

ANS_YES = 'yes'
ANS_NO = 'no'

count_password = int(input('Введите необходимое вам количество паролей '))
length_password = int(input('Введите длину пароля, от 6 до 20 символов '))
including_uppercase = input('Включать ли заглавные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?, yes/no ')
including_lowercase = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?, yes/no ')
including_chars = input('Включать ли символы!#$%&*+-=?@^_? (y/n)?, yes/no ')


def check_length_password(min_pass: int = 8,
                          max_pass: int = 32):
    # if not (min_pass <= length_password <= max_pass):
    if length_password not in range(min_pass, max_pass + 1):
        raise ValueError(
            f'Длина пароля от {min_pass} до {max_pass} символов'
        )
    return True


def is_including_digits() -> bool:
    choose = input(
        'Включать ли цифры 0123456789 ?, yes/no '
    ).lower()

    if choose not in ('yes', 'no'):
        raise ValueError(
            'Недопустимое значение'
        )

    return choose == 'yes'


def entered_user_data(digits, punctuation, lowercase, uppercase):
    """"
    Функция содержащая все символа, которые могут быть в пароле.
    """
    symbols = ''
    if is_including_digits():
        symbols += digits

    # TODO: 1. Переделать остальные проверки
    #  наподобие выше реализованной проверки
    if including_uppercase == 'yes':
        symbols += uppercase
    if including_lowercase == 'yes':
        symbols += lowercase
    if including_chars == 'yes':
        symbols += punctuation

    # if symbols == '':
    if not symbols:
        raise ValueError(
            'Выберите хотя бы один параметр'
        )

    return symbols


def generate_user_password():
    all_chars = entered_user_data(
        digits,
        punctuation,
        ascii_lowercase,
        ascii_uppercase
    )

    list_password = []
    if check_length_password():
        for _ in range(count_password):
            final_password = ''.join(
                random.choices(all_chars, k=length_password)
            )
            list_password.append(final_password)

    return list_password


print(*generate_user_password(), sep='\n')


def get_random_number(count: int,
                      start: int = 0,
                      end: int = 100) -> list[int] | None:
    """
    Сгенерирует указанное количество случайных чисел.

    :param count: Количество чисел.
    :param count: Начало диапазона.
    :param count: Конец диапазона.
    """

    # Обработка ошибочных моментов
    if count <= 0:
        print('Укажите натуральное число')
        return

    # Обработка ошибочных моментов
    if start > end:
        print('Начало диапазона должно быть меньше конца')
        return

    result = []
    while count > 0:
        rand_num = random.randint(start, end)
        result.append(rand_num)

        count -= 1

    return result


print(get_random_number(5, 100, 150))
print(get_random_number(7))

"""
3
10
no
yes
yes
yes
"""
