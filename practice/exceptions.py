
class MyException(Exception):
    def __init__(self, *args, **kwargs):
        self.status_code = kwargs.pop('status_code', None)
        super().__init__(*args, **kwargs)


def foo():
    raise MyException("Text", status_code=200)

try:
    foo()
except (IndexError, ZeroDivisionError) as exc:
    print(exc.status_code)

except ValueError:
    pass
except MyException as exc:
    print(exc, exc.status_code)
    raise
else:
    print("else")
finally:
    print("finally")

