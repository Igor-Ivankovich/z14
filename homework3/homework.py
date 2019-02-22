from itertools import zip_longest


def combine(_list1, _list2):
    """"Написать функцию, которая создаёт комбинацию
    двух списков таким образом:
    [a1, b1, c1, ...], [a2, b2, c2,...] -> [a1, a2, b1, b2, ...]
    """
    new_list = []
    list1_length = len(_list1)
    list2_length = len(_list2)
    max_length = max([list1_length, list2_length])
    for i in range(max_length):
        if i < list1_length:
            new_list.append(_list1[i])
        if i < list2_length:
            new_list.append(_list2[i])
    return new_list


def combine_v2(_list1, _list2):
    return list(
        filter(lambda x: x is not None, sum(zip_longest(_list1, _list2), ())))


def is_increase(_list):
    """
    Написать функцию, которая определяет , является ли список монотонно
    возрастающим(то есть верно ли, что каждый элемент
    этого списка больше предыдущего).
    """
    if not _list:
        return
    for i in range(len(_list) - 1):
        if not _list[i] < _list[i + 1]:
            return False
    return True


def is_increase_v2(_list):
    return _list == list(set(_list)) if _list else None


def max_number_count(_list):
    """
    Написать функцию, которая
    определяет в списке наиболее встречаемое значение.
    Вернуть значение и количество повторений.
    """
    _counter = {}
    for item in _list:
        _counter[item] = _counter.get(item, 0) + 1
    return max(_counter.items(), key=lambda x: x[1])


def get_anagrams(_str, _list):
    _str = sorted(_str)
    result = []
    for item in _list:
        if sorted(item) == _str:
            result.append(item)
    return result


def get_anagrams_v2(_str, _list):
    """
    Написать функцию, которая находит все
    анаграмы заданного слова из списка слов
    """
    _str = sorted(_str)
    return list(filter(lambda s: sorted(s) == _str, _list))


# ## HARD ## #
class Comparator:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        first_number = str(self.value) + str(other.value)
        second_number = str(other.value) + str(self.value)
        return second_number < first_number


def max_number(_list):
    """(*) Написать функцию, которая из списка чисел составляет
    максимальное число
    [98, 9, 34] -> 99834
    """
    if not _list:
        return
    sorted(_list, key=Comparator)

    return int(''.join(map(str, sorted(_list, key=Comparator))))


if __name__ == '__main__':
    assert combine([1, 2, 3], [4, 5, 6]) == [1, 4, 2, 5, 3, 6]
    assert combine([1, 2, 3], []) == [1, 2, 3]
    assert combine([1, 2], [3, 4, 5, 6]) == [1, 3, 2, 4, 5, 6]
    print('combine - OK')

    assert is_increase([1, 3, 4, 5]) is True
    assert is_increase([1, 3, 4, 4, 5]) is False
    assert is_increase([1, 6, 4]) is False
    assert is_increase([1]) is True
    assert is_increase([]) is None
    print('is_increase - OK')

    assert max_number_count([1, 2, 2, 3, 3, 3]) == (3, 3)
    assert max_number_count([1, 2, 3, 1, 1]) == (1, 3)
    print('max_number_count - OK')

    assert get_anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) == ['aabb', 'bbaa']  # noqa
    assert get_anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) == ['carer', 'racer']  # noqa
    assert get_anagrams('laser', ['lazing', 'lazy',  'lacer']) == []
    print('get_anagrams - OK')

    assert max_number([234, 123, 98]) == 98234123
    assert max_number([1, 2, 3, 4]) == 4321
    assert max_number([]) is None
    assert max_number([98, 9, 34]) == 99834
    print('max_number - OK')