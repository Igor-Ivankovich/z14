class MagicMethods:
    def __init__(self, value):
        self.value = value

    def __lshift__(self, other):
        return MagicMethods(self.value - other)

    def __rshift__(self, other):
        pass

    def __xor__(self, other):  # ^
        pass

    def __and__(self, other):  # &
        pass

    def __or__(self, other):  # |
        pass

    def __int__(self):
        pass

    def __float__(self):
        pass

    def __complex__(self):
        pass

    def __bool__(self):
        pass

    def __getattribute__(self, item):
        return object.__getattribute__(self, item)

    def __getitem__(self, item):
        return getattr(self, item)

    def __setitem__(self, key, value):
        return setattr(self, key, value)

    def __delitem__(self, item):
        return setattr(self, item, None)

    def __call__(self, *args, **kwargs):
        print(args, kwargs)


# METACLASSES

def square(self):
    return self.a * self.b

Rectangle = type('Rectangle', (), {
    'a': None,
    'b': None,
    'square': square
})
