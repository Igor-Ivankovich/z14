import time


class QueueException(Exception):
    pass


class Queue:
    def __init__(self, size=None):
        self.size = float('Inf') if size is None else size
        self._list = []

    def add(self, elem):
        if len(self._list) >= self.size:
            raise QueueException("add")
        else:
            self._list.append(elem)

    def pop(self):
        if not self._list:
            raise QueueException("pop")
        else:
            return self._list.pop(0)

    def get(self, index):
        if not self._list:
            raise QueueException("index")
        else:
            return self._list[index]

    def size(self):
        return len(self._list)

    @property
    def list(self):
        return self._list[::-1]


if __name__ == '__main__':
    q = Queue(20)
    while True:
        try:
            q.add(1)
        except QueueException as exc:
            if q.size > 100:
                break
            print("Smth went wrong!", str(exc))
            time.sleep(1)
            q.size += 20
