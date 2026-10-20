from linkedlist import LinkedList


class Stack:

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
        return reversed(list(self.list))

    def __str__(self):
        return str(list(self))

    def __eq__(self, other):
        return type(self) is type(other) and self.list == other.list

    def __add__(self, other):
        result = Stack(self)
        for item in other:
            result.push(item)
        return result

    def push(self, data):
        self.list.insert(0, data)

    def pop(self):
        return self.list.pop(0)

    def peek(self):
        return self.list[0]


def main():
    stack = Stack()

    for item in ("a", "b", "c"):
        stack.push(item)

    while not stack.isEmpty():
        print(stack.pop())


if __name__ == "__main__":
    main()
