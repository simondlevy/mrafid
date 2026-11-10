class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self, sourceCollection=None):
        self.head = None
        self.tail = None
        self._size = 0
        if sourceCollection is not None:
            for item in sourceCollection:
                self.append(item)

    def isEmpty(self):
        return self.head is None

    def __len__(self):
        return self._size

    def __iter__(self):
        point = self.head
        while point is not None:
            yield point.data
            point = point.next

    def __str__(self):
        return str(list(self))

    def __eq__(self, other):
        return type(self) is type(other) and list(self) == list(other)

    def __add__(self, other):
        result = LinkedList(self)
        for item in other:
            result.append(item)
        return result

    def __getitem__(self, index):
        if index < 0 or index >= len(self):
            raise IndexError("list index out of range")
        point = self.head
        for count in range(index):
            point = point.next
        return point.data

    def __setitem__(self, index, item):
        if index < 0 or index >= len(self):
            raise IndexError("list index out of range")
        point = self.head
        for count in range(index):
            point = point.next
        point.data = item

    def insert(self, index, item):
        if index < 0 or index > len(self):
            raise IndexError("list index out of range")
        if index == len(self):
            self.append(item)
            return

        node = Node(item)
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            point = self.head
            for count in range(index - 1):
                point = point.next
            node.next = point.next
            point.next = node
        self._size += 1

    def append(self, item):
        node = Node(item)
        if self.isEmpty():
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        self._size += 1

    def add(self, item):
        self.append(item)

    def pop(self, index=None):
        if index is None:
            index = len(self) - 1
        if index < 0 or index >= len(self):
            raise IndexError("list index out of range")

        if index == 0:
            node = self.head
            self.head = node.next
            if self.head is None:
                self.tail = None
        else:
            point = self.head
            for count in range(index - 1):
                point = point.next
            node = point.next
            point.next = node.next
            if node is self.tail:
                self.tail = point
        self._size -= 1
        return node.data

    def index(self, item):
        position = 0
        point = self.head
        while point.data != item:
            point = point.next
            position += 1
        return position

    def remove(self, item):
        self.pop(self.index(item))


def main():
    items = LinkedList()
    items.append("a")
    items.append("c")
    items.insert(1, "b")

    print(items)
    print(items.pop(0))
    print(items.pop())
    print(items)


if __name__ == "__main__":
    main()
