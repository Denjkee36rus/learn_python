import random
import math
n = int(input())
guess = random.randint(1, n + 1)

def ATTEMPT(guess):
    '''
    Находим, логориф двоичного числа, для
    нахождения количества попыток
    '''
    return math.ceil(math.log(guess, 2))
result = ATTEMPT(guess)

def game():
    attempt = 0
    while attempt <= result:
        user_number = int(input())
        if user_number == guess:
            print("Победа!!! Вы угадали !")
        elif user_number < guess:
            print('Загаданное число больше')
        elif user_number > guess:
            print('Загаданное число меньше')
        attempt += 1
    else:
        print(f'Вы проиграли, загаданное число {guess}')
        attempt += 1
game()




            # if guess == (1 + n) // 2:
        #     return "Победа, вы угадали число"
        # elif
# print(guess,"Количество попыток", ATTEMPT(guess))







