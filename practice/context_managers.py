
class MyContextManager:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        return self.name * 10

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Exit...')
        print(exc_type, exc_val, dir(exc_tb))
        print('#' * 30)


with MyContextManager("123") as text1:
    with MyContextManager("Text") as text:
        print(text1)
        print(text)


with MyContextManager("Text") as text, MyContextManager("Text123") as text1:
    print(text, text1)