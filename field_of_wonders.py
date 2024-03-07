import random

WORDS: list[str] = [
    'делить', 'ессентуки', 'накопать', 'панический', 'штопать'
]
random_word: str = random.choice(WORDS) # выбираем случайное слово

WORD: list[str] = list(random_word) # Делаем из случайного слова, список букв ['ш', 'т', 'о', 'п', 'а', 'т', 'ь']


stars: list[str] = list('*' * len(WORD)) # Подготавливаю список одинаковой длины, для сравнения с WORD list[]
letter = input('Какая буква?: ')  # о
for i in range(WORD):
    if letter in WORD:
        pass





# stars: list = ['*', '*', '*', '*', '*', '*']


# TODO: Проверить длину введенной строки, больше одной буквы указывать нельзя
print(WORD)
print(stars)
