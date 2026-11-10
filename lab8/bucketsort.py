"""
file: bucketsort.py
Author: Abrar Al Rafid
"""

import random
from time import perf_counter
from linkedlist import LinkedList
from sorts import quickSort


def bucketSort(lyst):
    if not lyst:
        return

    smallest = min(lyst)
    largest = max(lyst)
    buckets = [LinkedList() for _ in range(largest - smallest + 1)]

    for item in lyst:
        buckets[item - smallest].append(item)

    index = 0
    for bucket in buckets:
        for item in bucket:
            lyst[index] = item
            index += 1


def randints(n):
    return [random.randrange(n) for _ in range(n)]


def main():
    """Test bucketSort and print timing comparisons for different sizes."""
    random.seed(112)
    examples = [[], [5], [4, 1, 4, 0, 6, 1, 3],
                [3, 3, 3], [-2, 4, -2, 0], randints(10)]
    for lyst in examples:
        print("Before:", lyst)
        bucketSort(lyst)
        print("After: ", lyst)

    sizes = [10, 20, 50, 100, 250, 500]
    sizes += [1000 * 2 ** power for power in range(11)]
    print("n          BucketSort (s)  QuickSort (s)")
    for n in sizes:
        bucketList = randints(n)
        quickList = bucketList.copy()

        start = perf_counter()
        bucketSort(bucketList)
        bucketTime = perf_counter() - start

        start = perf_counter()
        quickSort(quickList)
        quickTime = perf_counter() - start

        print(f"{n:<10} {bucketTime:.9f}     {quickTime:.9f}")


if __name__ == "__main__":
    main()
