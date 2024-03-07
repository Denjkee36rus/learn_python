import random

WORDS: list[str] = [
    'делить', 'ессентуки', 'накопать', 'панический', 'штопать'
]
random_word: str = random.choice(WORDS)  # выбираем случайное слово


def get_all_index_for_letter(text: str, char: str) -> list[int]:
    """
    Получает строку и символ, возвращает список индексов символа в строке.
    :param text: Строка текста.
    :param char: Символ, для которого нужно найти все индексы в строке.
    """
    result: list[int] = []

    for index in range(len(text)):
        if text[index] == char:
            result.append(index)

    return result


def set_letter_for_all_index(
        indexes: list[int],  # [1, 3, 5]
        hide_word: list[str],  # ['*', '*', '*', '*', '*', '*'],
        letter: str  # к
) -> None:
    for index in indexes:
        hide_word[index] = letter

    # return hide_word


def field_of_wonders_game():
    word_length: int = len(random_word)
    stars: list[str] = ['*'] * word_length
    while '*' in stars:
        letter: str = input('Какая буква?: ')

        if letter in random_word:
            list_of_index: list[int] = get_all_index_for_letter(
                random_word, letter
            )
            set_letter_for_all_index(
                list_of_index, stars, letter
            )

            # stars = set_letter_for_all_index(list_of_index, stars, letter)

            print(*stars, sep=' | ')
        else:
            print('Буква "{letter}" нет в слове, '
                  f'длина слова {word_length} букв')

    print('Победа!')


if __name__ == '__main__':
    field_of_wonders_game()
