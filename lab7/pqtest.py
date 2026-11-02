"""
pqtest.py
Abrar Al Rafid
"""

import random
import time

from priorityqueue import PriorityQueue as PQ1
from priorityqueue2 import PriorityQueue as PQ2


def main():
    old_queue = PQ1()
    new_queue = PQ2()

    for value in [5, 1, 3, 1, 4]:
        old_queue.push(value)
        new_queue.push(value)

    removed = []
    while not old_queue.isEmpty():
        removed.append(old_queue.pop())
    print("Old queue:", removed, "Expected: [1, 1, 3, 4, 5]")

    removed = []
    while not new_queue.isEmpty():
        removed.append(new_queue.pop())
    print("New queue:", removed, "Expected: [1, 1, 3, 4, 5]")

    for size in [1000, 2000, 4000]:
        values = list(range(size))
        random.shuffle(values)

        old_queue = PQ1()
        new_queue = PQ2()

        print("\nTesting", size, "items")
        print("Adding to the old queue, expected to take some time.", flush=True)
        start = time.perf_counter()
        for value in values:
            old_queue.push(value)
        old_time = time.perf_counter() - start

        print("Adding to the new queue.", flush=True)
        start = time.perf_counter()
        for value in values:
            new_queue.push(value)
        new_time = time.perf_counter() - start

        print("Old queue seconds:", old_time)
        print("New queue seconds:", new_time)


if __name__ == "__main__":
    main()
