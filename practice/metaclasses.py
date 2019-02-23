class Singleton(type):
    _objects = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._objects:
            cls._objects[cls] = type.__call__(cls, *args, **kwargs)
        return cls._objects[cls]


class MyClass(metaclass=Singleton):
    def __init__(self, name):
        self.name = name

m1 = MyClass(name="1")
print(m1.name)

m2 = MyClass(name="2")
print(m2.name)
print(m1 == m2, m1 is m2)

