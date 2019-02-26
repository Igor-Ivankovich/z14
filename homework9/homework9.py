"""
0.
Продолжаем задачу на фигруры.
Параметры каждой фигуры должны быть дескрипторами.
Дескриптор должен валидировать переданное значение.
Используя дескрипторы, проверьте правильность введённых данных (a, b, c, r > 0).
square и perimeter -  теперь тоже дескрипторы. Обратите внимание, что при каждом обращении к square/perimeter
значения будут вычисляться заново. Подумайте, как это можно обойти,
т.е. значение должно вычисляться только при первом обращении к дескриптору.
Если меняется один из атрибутов фигуры ( например r), то необходимо заново пересчитать square или perimeter
"""
import time

"""
1.
Напишите менеджер контекста MultiFileOpen, который позволяет работать с несколькими файлами:
MultiFileOpen(('file1.txt', 'r'), ('file2.txt', 'w'), ..., ('fileN.txt', 'rb'))
"""


class MultiFileOpen:
    def __init__(self, *args):
        self.list_file = args
        self._opened_files = None

    def __enter__(self):
        self._opened_files = map(lambda x: open(*x), self.list_file)
        return self._opened_files

    def __exit__(self, exc_type, exc_val, exc_tb):
        for file in self._opened_files:
            file.close()

"""
2.
Напишите менеджер контекста Timer, который позволяет получать текущее время выполнения кода (отсчет начинается с конструкции with):
with Timer("Time: {}") as timer:
    do_some_logic()
    print(timer.now())  # Time: 3.4123 sec
    do_some_other_logic()
    print(timer.now())  # Time: 5.71 sec
"""


class Timer:
    def __init__(self, _str):
        self._str = _str
        self.start = 0

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def now(self):
        return self._str.format(time.time() - self.start)

with Timer("Text {}") as timer:
    print(timer.now())


"""
3.
Напишите генератор fibonacci(n), который генерирует числа Фибоначчи до n включительно.
"""



"""
4.
Напишите класс, объектом которого будет итератор производящий только чётные числа до n включительно.
"""


"""
5.
Напишите генератор factorials(n), генерирующий последовательность факториалов натуральных чисел.
"""


"""
6.*
Напишите генератор BinomialCoefficients(n), генерирующий последовательность биномиальных коэффициентов C0n,C1n,…,Cnn
Запрещается использовать факториалы.
"""


class BinomialCoefficients:
    def __init__(self, n):
        self.n = n + 1
        self.numerator = 1
        self.divider = 1
        self.index = 1

    def __next__(self):
        if self.index > self.n:
            raise StopIteration
        coef = self.numerator // self.divider
        self.numerator *= (self.n - self.index)
        self.divider *= self.index
        self.index += 1
        return coef

    def __iter__(self):
        return self


"""
7.*
Напишите метакласс, который возводит имена всех аттрибутов класса в верхний регистр.
"""