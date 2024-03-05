from mathematics import factorial
from validators import is_palindrome, is_prime


def test_factorial():
    test_case: int = 3

    expected: int = 6
    result: int = factorial(test_case)

    assert result == expected, f'Ожидается {expected}, получено {result}'


def test_palindrome():
    test_case: str = 'мадам'

    expected: bool = True
    result: bool = is_palindrome(test_case)

    assert result == expected, f'Ожидается {expected}, получено {result}'


test_factorial()
test_palindrome()

print('Тесты успешно пройдены')
