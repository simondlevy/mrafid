from queue import Queue

class PriorityQueue(Queue):

    def push(self, data):
        if self.isEmpty() or data >= self.list.tail.data:
            Queue.push(self, data)
            return len(self)

        point = self.list.head
        position = 0
        while data >= point.data:
            point = point.next
            position += 1

        self.list.insert(position, data)
        return position + 1


def main():
    queue = PriorityQueue()

    for item in ("c", "a", "d", "b", "f", "e"):
        queue.push(item)

    while not queue.isEmpty():
        print(queue.pop())


if __name__ == "__main__":
    main()
