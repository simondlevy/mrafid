"""
priorityqueue2.py
Abrar Al Rafid
"""

from heap import Heap


class PriorityQueue:

    def __init__(self, sourceCollection=None):
        self.heap = Heap(sourceCollection)

    def isEmpty(self):
        return self.heap.isEmpty()

    def __len__(self):
        return len(self.heap)

    def __contains__(self, item):
        return item in self.heap

    def __iter__(self):
        return iter(self.heap)

    def __str__(self):
        return str(list(self))

    def __eq__(self, other):
        return type(self) is type(other) and list(self) == list(other)

    def __add__(self, other):
        result = PriorityQueue(self)
        for item in other:
            result.push(item)
        return result

    def push(self, datum):
        self.heap.add(datum)

    def add(self, datum):
        self.push(datum)

    def pop(self):
        return self.heap.pop()

    def peek(self):
        return self.heap.peek()


def test_priorityqueue():
    queue = PriorityQueue()
    print("Empty:", queue.isEmpty(), "Expected: True")

    for value in [3, 1, 3, 2]:
        queue.push(value)

    print("Queue:", queue, "Expected: [1, 2, 3, 3]")
    print("Length:", len(queue), "Expected: 4")
    print("Next item:", queue.peek(), "Expected: 1")
    print("Contains 2:", 2 in queue, "Expected: True")
    print("Contains 9:", 9 in queue, "Expected: False")

    removed = []
    while not queue.isEmpty():
        removed.append(queue.pop())
    print("Removed:", removed, "Expected: [1, 2, 3, 3]")
    print("Empty now:", queue.isEmpty(), "Expected: True")


if __name__ == "__main__":
    test_priorityqueue()
