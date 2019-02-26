import math
import abc


# 1.
# ## HARD ## #
from datetime import datetime


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
    assert max_number([234, 123, 98]) == 98234123
    assert max_number([1, 2, 3, 4]) == 4321
    assert max_number([]) is None
    assert max_number([98, 9, 34]) == 99834
    print('max_number - OK')


class LoggerMixin:
    def log(self):
        print(datetime.now().isoformat(), str(self))


class FigureException(Exception):
    pass


class PositiveNumberDescriptor:
    def __init__(self, name):
        self.name = name

    def _validate(self, value):
        if value <= 0:
            raise FigureException("Value <= 0")

    def __set__(self, instance, value):
        self._validate(value)
        setattr(instance, self.name, value)
        setattr(instance, 'calculated', False)

    def __get__(self, instance, owner):
        return getattr(instance, self.name, None)


class CacheDescriptor:
    def __init__(self, name):
        self.name = name
        self.func = None

    def __get__(self, instance, owner):
        if not getattr(instance, 'calculated') or \
                not getattr(instance, self.name, None):
            setattr(instance, self.name, self.func())
            setattr(instance, 'calculated', True)
            print('miss cache')
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.func = value


class AttrsMeta(abc.ABCMeta):
    def __new__(cls, object_or_name, bases, _dict):
        _dict['calculated'] = False
        for key in _dict.get('args', []):
            _dict[key] = PositiveNumberDescriptor(f'_{key}')
        return type.__new__(cls, object_or_name, bases, _dict)


class TestClass:
    a = PositiveNumberDescriptor("_a")


class Figure(metaclass=AttrsMeta):
    args = ()

    perimeter = CacheDescriptor('_perimeter_cache')
    square = CacheDescriptor('_square_cache')

    def __init__(self, name, **kwargs):
        self.validate(**kwargs)
        self.name = name
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.perimeter = self._perimeter
        self.square = self._square

    def validate(self, **kwargs):
        for arg in self.args:
            if kwargs[arg] <= 0:
                raise FigureException(f"{kwargs[arg]} <= 0")

    def _perimeter(self):
        return 'Not implemented'

    # @abc.abstractmethod
    def _square(self):
        pass

    def __eq__(self, other):
        return self.square() == other.square()
    
    def __str__(self):
        return f'{self.__class__.__name__}: {self.name}'


class Triangle(Figure):
    args = ('a', 'b', 'c')

    def validate(self, **kwargs):
        super().validate(**kwargs)
        if kwargs['a'] + kwargs['b'] <= kwargs['c'] \
                or kwargs['a'] + kwargs['c'] <= kwargs['b'] \
                or kwargs['c'] + kwargs['b'] <= kwargs['a']:
            raise FigureException("Invalid args")

    def _perimeter(self):
        return self.a + self.b + self.c

    def _square(self):
        p = self.perimeter / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5


class Circle(Figure):
    args = ('r',)

    def _perimeter(self):
        return 2 * self.r * math.pi

    def _square(self):
        return math.pi * self.r ** 2


class Rectangle(Figure, LoggerMixin):
    args = ('a', 'b')

    def _perimeter(self):
        return 2 * (self.a + self.b)

    def _square(self):
        return self.a * self.b


class Star(Figure):

    def _square(self):
        return 42


class Star6(Figure):
    pass

"""
2.
Создайте класс Figure. У каждой фигуры есть имя, также можно найти площадь и периметр фигуры (методы square и perimeter).
Создайте классы Triangle, Circle, Rectangle производные от Figure. 
У класса Triangle есть 3 стороны: a, b, c; у Circle - радиус r; у Rectangle - стороны a и b. 
Переопределите методы нахождения площади и периметра для каждой фигуры (Triangle, Circle, Rectangle). 
Также для объектов классов должны работать операторы сравнения: ==, >, < <=, >=. 
Будем считать, что фигуры равны, если они имеют одинаковую площадь. 
Строковое представление объекта должно возвращать тип фигуры и её имя в следующем формате:
например для Circle(name='abc', r=2) - Circle:"abc"
Также необходимо обработать возможные исключения: r, a, b, c > 0, треугольник существует, если сумма любых двух сторон больше третьей.
Инче должно быть выброшено соответствующее исключение, классы исключений определить самостоятельно.
Дополнительная функциональность приветствуется.
"""

"""
if __name__ == '__main__':
    circles = [Circle(name=f'r={i}', r=i) for i in range(1, 5)]
    rectangles = [Rectangle(name=f'a={i}, b={i**2}', a=i, b=i**2) for i in range(1, 5)]
    triangles = [Triangle(name=f'a={i+1}, b={i**2}, c={(i + i**2)//2}', a=i+1, b=i**2, c=(i + i**2)//2) for i in range(1, 4)]

    figures = circles + triangles + rectangles
    for figure in figures:
        print(f'My name is: {figure}')
        assert str(figure) == f'{figure.__class__.__name__}:"{figure.name}"'
        print(f'My perimeter is: {figure.perimeter()}')
        print(f'My square is: {figure.square()}', end=f"\n{'-'*35}\n")

    assert Circle(name='1', r=2) == Circle(name='2', r=2)
    assert Circle(name='1', r=2) < Circle(name='2', r=4)
    assert Circle(name='1', r=4) >= Circle(name='2', r=4)


    assert Rectangle(name='1', a=2, b=3) == Rectangle(name='2', b=2, a=3)
    assert Rectangle(name='1', a=2, b=3) < Rectangle(name='2', a=4, b=10)
    assert Rectangle(name='1', a=4, b=2) >= Rectangle(name='2', a=4, b=1)

    assert Triangle(name='1', a=2, b=3, c=4) == Triangle(name='2', b=2, a=3, c=4)
    assert Triangle(name='1', a=2, b=3, c=1.5) < Triangle(name='2', a=4, b=10, c=7)
    assert Triangle(name='1', a=4, b=2, c=5) >= Triangle(name='2', a=4, b=5, c=1)
"""
