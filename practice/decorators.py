import time


def timer(func):
    def _func(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(time.time() - start)
        return result
    return _func


def timer_with_arg(text):
    def _decorator(func):
        def _inner(*args, **kwargs):
            print(text)
            return func(*args, **kwargs)
        return _inner
    return _decorator


@timer
def factorial(n):
    result = 1
    while n:
        result *= n
        n -= 1
    return result

# factorial = timer(factorial)
# print(factorial.__name__)
if __name__ == '__main__':
    print(factorial(100))

# factorial = timer(timer_with_arg("Hello")(factorial))

# print(factorial(100))
