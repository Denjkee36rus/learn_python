import random

positives = [
    'Бесспорно', 'Предрешено', 'Никаких сомнений',
    'Определённо да', 'Можешь быть уверен в этом'
]

small_positive = [
    'Мне кажется - да', '	Вероятнее всего'
]

neutral = [
    'Пока неясно, попробуй снова', 'Спроси позже'
]

negative = [
    'Даже не думай', 'Мой ответ - нет'
]

# answers = [
#     'Мне кажется - да', 'Пока неясно', 'попробуй снова', 'Даже не думай',
#     'Предрешено', 'Вероятнее всего', 'Спроси позже', 'Мой ответ - нет',
#     'Предрешено', 'Вероятнее всего', 'Спроси позже', 'Мой ответ - нет',
#     'Никаких сомнений', 'Хорошие перспективы', 'Лучше не рассказывать', 'По моим данным - нет',
#     'Определённо да', 'Знаки говорят - да', 'Сейчас нельзя предсказать', 'Перспективы не очень хорошие',
#     'Можешь быть',  'уверен в этом!', 'Да', 'Сконцентрируйся и спроси опять', 'Весьма сомнительно'
# ]

part_1 = random.choice(positives)
part_2 = random.choice(small_positive)
part_3 = random.choice(neutral)
part_4 = random.choice(negative)


answers = [
    positives, small_positive, neutral, negative
]

print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
name = input('как тебя зовут ?')
print('Привет', name)
while True:
    user_question = input('Задайте вопрос:')
    elem = random.choice(answers)
    print(elem)

    # print(random.choice(elem))
    print(f'{part_1} {part_2} {part_3} {part_4}')
    print('Хочешь еще спросить, что-то ?')
    user_answers = input()
    if user_answers.lower() == 'да':
        continue
    elif user_answers.lower() == 'нет':
        print('Возвращайся если возникнут вопросы!')
        break
    else:
        print('Приходи еще!')
        break
