import random
import time


def some_function(arg):
    time.sleep(3)
    return random.randint(1, 1000)


def some_function_other():
    number = random.randint(1, 1000000)
    if number == 666:
        raise Exception('SOTONA')
    return number


def other_function(arg=None):
    result = some_function(arg)
    some_function_other()

    if result % 2 == 1:
        return 98
    return 42


def foo():
    try:
        some_function_other()
    except Exception:
        return "error"
    else:
        return "ok"
