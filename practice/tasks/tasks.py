import re
import doctest


def sort_words(_str):
    """
    >>> sort_words("4of Fo1r pe6ople g61oo3d th5e the2")
    'Fo1r the2 4of th5e pe6ople g61oo3d'

    >>> sort_words("raise")
    Traceback (most recent call last):
    ...
    ValueError

    """
    if _str == 'raise':
        raise ValueError
    _str = _str.split()
    pattern = re.compile("\d+")
    # _str = sorted(_str, key=lambda word: [sym for sym in word if sym.isdigit()][0])
    _str = sorted(_str, key=lambda word: pattern.findall(word))
    return ' '.join(_str)


if __name__ == '__main__':
    doctest.testmod()