"""
heap.py
Abrar Al Rafid
"""


class Heap:

    def __init__(self, sourceCollection=None):
        self._heap = []
        if sourceCollection is not None:
            for item in sourceCollection:
                self.add(item)

    def isEmpty(self):
        return len(self._heap) == 0

    def __len__(self):
        return len(self._heap)

    def __contains__(self, item):
        return item in self._heap

    def __str__(self):
        return str(self._heap)

    def __iter__(self):
        copy = Heap(self._heap)
        items = []
        while not copy.isEmpty():
            items.append(copy.pop())
        return iter(items)

    def add(self, item):
        self._heap.append(item)
        position = len(self._heap) - 1
        while position > 0:
            parent = (position - 1) // 2
            if self._heap[parent] <= item:
                break
            self._heap[position] = self._heap[parent]
            self._heap[parent] = item
            position = parent

    def peek(self):
        if self.isEmpty():
            raise IndexError("peek at an empty heap")
        return self._heap[0]

    def pop(self):
        if self.isEmpty():
            raise IndexError("pop from an empty heap")

        top_item = self._heap[0]
        bottom_item = self._heap.pop()
        if self.isEmpty():
            return top_item

        self._heap[0] = bottom_item
        position = 0

        while True:
            left_child = 2 * position + 1
            right_child = 2 * position + 2

            if left_child >= len(self._heap):
                break

            smaller_child = left_child
            if right_child < len(self._heap):
                if self._heap[right_child] < self._heap[left_child]:
                    smaller_child = right_child

            if bottom_item <= self._heap[smaller_child]:
                break

            self._heap[position] = self._heap[smaller_child]
            self._heap[smaller_child] = bottom_item
            position = smaller_child

        return top_item


def test_heap():
    heap = Heap()
    print("Empty:", heap.isEmpty(), "Expected: True")
    print("Empty heap:", heap, "Expected: []")

    for value in [5, 3, 1, 3]:
        heap.add(value)

    print("Heap:", heap, "Expected: [1, 3, 3, 5]")
    print("Contains 3:", 3 in heap, "Expected: True")
    print("Contains 9:", 9 in heap, "Expected: False")
    print("Smallest:", heap.peek(), "Expected: 1")
    print("In order:", list(heap), "Expected: [1, 3, 3, 5]")
    print("Length:", len(heap), "Expected: 4")

    removed = []
    while not heap.isEmpty():
        removed.append(heap.pop())
    print("Removed:", removed, "Expected: [1, 3, 3, 5]")
    print("Empty now:", heap.isEmpty(), "Expected: True")

if __name__ == "__main__":
    test_heap()
