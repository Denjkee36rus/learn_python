def is_prime(num: int) -> bool:
    """
    Проверяет, является ли число простым.
    :param num: Натуральное число.
    """
    pass


def is_palindrome(text: str) -> bool:
    """Проверяет, является ли строка палиндромом.
    Читается одинаков слева направо и справа налево.
    :param text: Строка текста.
    """

    return text == text[::-1]
