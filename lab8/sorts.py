"""
Author: Abrar Al Rafid
File: sorts.py

Defines the selection sort and the quick sort.
"""
from counter import Counter
from tools import getRandomList

def selectionSort(lyst, comps = None, swaps = None):
    """Sorts lyst with a selection sort."""
    n = len(lyst)
    for i in range(n):
        minIndex = minInRange(lyst, i, n, comps)
        if minIndex != i:
            swap(lyst, i, minIndex, swaps)

def minInRange(lyst, i, n, comps = None):
    minValue = lyst[i]
    minIndex = i
    for j in range(i, n):
        if comps is not None:
            comps.increment()
        if lyst[j] < minValue:
            minValue = lyst[j]
            minIndex = j
    return minIndex

def quickSort(lyst, comps = None, swaps = None):
    def recurse(left, right):
        if left < right:
            pivotPosition = partition(lyst, left, right)
            recurse(left, pivotPosition - 1);
            recurse(pivotPosition + 1, right)

    def partition(lyst, left, right):
                # Find the pivot and exchange it with the last item
        middle = (left + right) // 2
        pivot = lyst[middle]
        lyst[middle] = lyst[right]
        lyst[right] = pivot
        # Set boundary point to first position
        boundary = left
        # Move items less than pivot to the left
        for index in range(left, right):
            if comps is not None:
                comps.increment()
            if lyst[index] < pivot:
                swap(lyst, index, boundary, swaps)
                boundary += 1
        # Exchange the pivot item and the boundary item
        swap(lyst, right, boundary, swaps)
        return boundary

    recurse(0, len(lyst) - 1)

def swap(lyst, i, j, counter = None):
    """Exchanges the items at i and j in lyst and increments
    the counter if it exists."""
    if counter: counter.increment()
    lyst[i], lyst[j] = lyst[j], lyst[i]       

def test(sort, n = 15):
    """Runs some tests on a sort function."""
    lyst = list(range(1, n + 1))
    print("Sorting", lyst)
    sort(lyst)
    print("Result", lyst)
    lyst = getRandomList(n)
    print("Sorting", lyst)
    sort(lyst)
    print("Result", lyst)

def testWithCounters(sort, n = 15):
    """Runs some tests on a sort function."""
    comps = Counter()
    swaps = Counter()
    lyst = list(range(1, n + 1))
    print("Sorting", lyst)
    sort(lyst, comps, swaps)
    print("Result", lyst, "Comps:", str(comps), "Swaps:", str(swaps))
    comps.reset()
    swaps.reset()
    lyst = getRandomList(n)
    print("Sorting", lyst)
    sort(lyst, comps, swaps)
    print("Result", lyst, "Comps:", str(comps), "Swaps:", str(swaps))


def main():
    """To test, pass the name of the sort function to test."""
    test(selectionSort)
    testWithCounters(selectionSort)
    testWithCounters(selectionSort, n = 150)
    test(quickSort)
    testWithCounters(quickSort, n = 150)

if __name__ == "__main__":
    main()
