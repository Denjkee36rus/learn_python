PI: float = 3.14159268


def factorial(num: int) -> int:
    """
    Вычисляет факториал числа, принимает одно натуральное число.
    :param num: Натуральное число.
    """
    # if not isinstance(num, int):
    if type(num) != int:
        raise TypeError(
            f'Функция принимает целое число, Вы передали {type(num)}'
        )
    if num < 1:
        raise ValueError(
            'Факториал определен только для натуральных чисел'
        )

    prod: int = 1
    for n in range(1, num + 1):
        prod *= n  # prod = prod * n

    return prod
