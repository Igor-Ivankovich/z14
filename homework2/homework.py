def max_number(a, b, c):
    if a > b and a > c:
        _max = a
    elif b > a and b > c:
        _max = b
    else:
        _max = c
    return _max


# 1. Создать функцию которая создает список
# натуральных чисел от минимума до максимума с шагом
def custom_range(_min, _max, _step=1):
    result = []
    while _min < _max:
        result.append(_min)
        _min += _step
    return result


# 2. Написать функцию, которая вычисляет факториал заданого числа
def factorial(n):
    result = 1
    while n:
        result *= n
        n -= 1
    return result


# def factorial(n):
#     return n * factorial(n - 1) if n > 1 else 1


# 3. Написать функцию которая определяет
# сколько чисел списка больше по модулю максимального.
# Для нахождения модуля
# использовать функцию abs
def count_of_max_numbers(_list):
    count = 0
    if not _list:
        return count
    _max = _list[0]
    for item in _list:
        if item > _max:
            _max = item

    for item in _list:
        if abs(item) > _max:
            count += 1
    return count


if __name__ == '__main__':
    assert custom_range(1, 4) == [1, 2, 3]
    assert custom_range(1, 4, 2) == [1, 3]
    assert custom_range(1, 1, 2) == []
    print('1 - OK')

    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(20) == 2432902008176640000
    print('2 - OK')

    assert count_of_max_numbers([]) == 0
    assert count_of_max_numbers([1]) == 0
    assert count_of_max_numbers([5, 7, -10, -8]) == 2
    print('3 - OK')

