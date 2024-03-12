# FIFO - First In First Out - Первым пришел первым ушел
queue = ['H1', 'H2', 'H3', 'H4']


def process():
    i: int = 0
    while i < len(queue):
        print(f'Обслуживаем персона: {queue[i]}')
        queue.pop(i)
        print(f'В очереди {len(queue)} человек')
        print('-------------------------------------')

        new_person = input('Добавить кого-то в очередь?: ')
        if new_person:
            queue.append(new_person)
            print(f'В очереди {len(queue)} человек')


# if __name__ == '__main__':
process()
