import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'


count_password = int(input('Введите необходимое вам количество паролей'))
length_password = int(input('Введите длину пароля, от 6 до 20 символов'))
including_numbers = input('Включать ли цифры 0123456789 ?, yes/no')
including_uppercase = input('Включать ли заглавные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?, yes/no')
including_lowercase = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?, yes/no')
including_chars = input('Включать ли символы!#$%&*+-=?@^_? (y/n)?, yes/no')

def check_length_password():
    if length_password < 6 or length_password > 20:
        print('Пароль должен состоять и чисел от 6 до 20 символов')
        return False
    else:
        return True


def entered_user_data():
    """"
    Функция содержащая все символа, которые
    могут быть в пароле
    """
    symbols = ''
    if including_numbers == 'yes':
        symbols += digits
    if including_uppercase == 'yes':
        symbols += uppercase_letters
    if including_lowercase == 'yes':
        symbols += lowercase_letters
    if including_chars == 'yes':
        symbols += punctuation
    return symbols
def generate_user_password():
    final_password = ''
    if check_length_password():
        for _ in range(count_password):
            for i in range(length_password):
                final_password += random.choice(entered_user_data())
        print(final_password, sep='\n')
print(generate_user_password())


