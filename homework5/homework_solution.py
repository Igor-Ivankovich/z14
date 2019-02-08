import re

"""
1.
Написать декоратор, который считает сколько раз была вызвана функция и выводит
эту информации на экран.
В качестве аргумента(необязательного) декоратор может принимать
текст(форматированный), который
будет выводиться вместе с количеством вызовов. Если данный аргумент не передан,
то выводить текст по умолучанию(любой)

@counter():
def foo():
    return 1

foo(123)
>>> 'Count - 1'
>>> 1
foo("asd")
>>> 'Count - 2'
>>> 1

@counter("Text {}"):
def foo1():
    return 1
>>> 'Text 1'
>>> 1
"""


def counter(text='Default {}'):
    def wrapper(func):
        def new_func(*args, **kwargs):
            new_func.count = getattr(new_func, 'count', 0) + 1
            print(text.format(new_func.count))
            return func(*args, **kwargs)
        return new_func
    return wrapper


"""
2.
Написать функцию, которая извлекает даты из строки.'

get_datetimes('Lorem Ipsum is simply 12-01-2018 dummy text of
the printing 10-13-2018 and typesetting industry.
10-02-2018 Lorem Ipsum has been the industry a s x')
>>> ['12-01-2018', '10-02-2018', '10-13-2018']
"""

def get_datetimes(_str):
    pattern = re.compile(r'\b(\d{2}-\d{2}-\d{2,4})\b')
    return pattern.findall(_str)


"""
3.
Написать функцию, которая извлекает все слова,
начинающиеся на гласную(согласную). Какие слова извлекать - аргумент функции
get_words('Lorem Ipsum is simply', sym=('consonants', 'vowels'))
>>> ['Lorem', 'Ipsum', 'is', 'sumply']

get_words('Lorem Ipsum is simply', sym=('consonants',))
>>> ['Lorem', 'sumply']

get_words('Lorem Ipsum is simply', sym=('vowels',))
>>> ['Ipsum', 'is']
"""

def get_words(_str, sym=('consonants', 'vowels')):
    consonants = 'consonants'
    vowels = 'vowels'
    patter_1 = re.compile(r'\b[aeuioy]\w+\b', flags=re.IGNORECASE | re.UNICODE)
    patter_2 = re.compile(r'\b[^aeuioy]\w+\b', flags=re.IGNORECASE | re.UNICODE)
    result = []
    if consonants in sym and vowels in sym:
        result = patter_1.findall(_str) + patter_2.findall(_str)
    elif consonants in sym:
        result = patter_1.findall(_str)
    elif vowels in sym:
        result = patter_2.findall(_str)
    return result


def get_words_new(_str, sym=('consonants', 'vowels')):
    _dict = {
        ('consonants', 'vowels'): re.compile(r'\b\w+\b',
                                             flags=re.IGNORECASE | re.UNICODE),
        ('consonants',): re.compile(r'\b[aeuioy]\w+\b',
                                    flags=re.IGNORECASE | re.UNICODE),
        ('vowels', ): re.compile(r'\b[^aeuioy]\w+\b',
                                 flags=re.IGNORECASE | re.UNICODE)
    }
    pattern = _dict.get(sym)
    if pattern:
        return pattern.findall(_str)


"""
4. Написать функцию, которая группирует результат команды ping
((<icmp_seq>, <ttl>), ...)

s = '''64 bytes from 216.58.215.110: icmp_seq=0 ttl=54 time=30.391 ms
64 bytes from 216.58.215.110: icmp_seq=1 ttl=54 time=30.667 ms
64 bytes from 216.58.215.110: icmp_seq=2 ttl=54 time=33.201 ms
64 bytes from 216.58.215.110: icmp_seq=3 ttl=54 time=30.140 ms
64 bytes from 216.58.215.110: icmp_seq=4 ttl=54 time=31.822 ms'''
get_result(s)
>>> ((0, 30.391), (1, 30.667), (2, 33.201), (3, 30.140), (4, 31.822))
"""


def get_result(_str):
    pattern = re.compile(r'\bicmp_seq=(\d+).*time=([\d.\d]+)')
    return tuple(
        map(lambda x: (int(x[0]), float(x[1])), pattern.findall(_str)))


