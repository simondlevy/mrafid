from linkedlist import LinkedList


class Queue:

    def __init__(self, sourceCollection=None):
        self.list = LinkedList()
        if sourceCollection is not None:
            for item in sourceCollection:
                self.push(item)

    def isEmpty(self):
        return self.list.isEmpty()

    def __len__(self):
        return len(self.list)

    def __iter__(self):
        return iter(self.list)

    def __str__(self):
        return str(list(self))

    def __eq__(self, other):
        return type(self) is type(other) and self.list == other.list

    def __add__(self, other):
        result = type(self)(self)
        for item in other:
            result.push(item)
        return result

    def push(self, data):
        self.list.append(data)

    def add(self, item):
        return self.push(item)

    def pop(self):
        return self.list.pop(0)

    def peek(self):
        return self.list[0]


def main():
    queue = Queue()

    for item in ("a", "b", "c"):
        queue.push(item)

    while not queue.isEmpty():
        print(queue.pop())


if __name__ == "__main__":
    main()
