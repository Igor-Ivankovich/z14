def my_max(_list):
    max_number = _list[0]
    for item in _list:
        if item > max_number:
            max_number = item
    return max_number

print(my_max([4, 3, 5, 10]))
print(my_max([8, 3, 5, 11]))


def foo(a, b, c):
    return

foo(a=1, c=3, b=2)
foo(1, 2, c=3)


def create_user(first_name, last_name, address, age):
    return

create_user(
    first_name='Tima',
    last_name='Akulich',
    address='asdas',
    age=25
)


def foo1(a, b, c=None):
    return

foo1(1, 2, 3)
foo1(1, 2)


def max_new(*args):
    max_number = args[0]
    for item in args:
        if item > max_number:
            max_number = item
    return max_number

print(max_new(1, 2, 3, 4, 3))


def foo2(a, *args):
    print(a, args)

foo2(1, 2, 3, 4)


def foo3(**kwargs):
    print(kwargs)

foo3(first_name="Tima", last_name="Akulich")


def foo4(a, b, *args, **kwargs):
    pass
print('Text', foo4(1, 2))
