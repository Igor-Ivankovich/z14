
class Stack:
    def __init__(self, size=None):
        self.size = float('Inf') if size is None else size
        self._list = []

    def add(self, elem):
        if len(self._list) >= self.size:
            print("Error 'add'")
        else:
            self._list.append(elem)

    def pop(self):
        if not self._list:
            print("Error 'pop'")
        else:
            return self._list.pop(-1)

    def size(self):
        return len(self._list)

    def to_string(self):
        for item in self._list[::-1]:
            print('| ', str(item).center(5, ' '), ' |')
        print('_' * 9)
