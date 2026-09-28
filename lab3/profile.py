"""
Author: Abrar Al Rafid
File: profile.py

Resources for profiling sort and fibonacci functions.
"""

import time
from counter import Counter
from tools import getRandomList
from fibs import fib1, fib2
from sorts import selectionSort, quickSort
                    
def profileSort(sortFunction, upper = 10):
    """Displays counts of comparisons and swaps
    and running times for the given sort algorithm
    on several data sizes.  The data size starts at 1
    and doubles on each iteration.  An initial run
    shows results for a sorted list of 256 numbers.
    Arguments: the sort function and the number of data sets."""
    comps = Counter()
    swaps = Counter()
    lyst = list(range(1, 257))
    t1 = time.time()
    sortFunction(lyst, comps, swaps)
    t2 = time.time() - t1
    print("Results for a sorted list of 256 numbers:")
    print("Comparisons:    ", comps)
    print("Swaps:          ", swaps)
    print("Time in seconds:", t2)
    size = 1
    print("\n Size    Comparisons     Swaps   Running Time (sec)")
    for i in range(1, upper + 1):
        comps.reset()
        swaps.reset()
        lyst = getRandomList(size)
        t1 = time.time()
        sortFunction(lyst, comps, swaps)
        t2 = time.time() - t1
        print("%5d%12s%12s%15.6f" % (size, comps, swaps, t2))
        size *= 2

def profileFib(fibFunction, upper = 20):
    """Displays counts of calls and running times
    of the given fib function on several values of n.
    Arguments: the fib function and the upper bound
    on n.  n increases by 1 on each iteration."""
    n = 1
    counter = Counter()
    print(" n     fib(n)     # Call  Running Time (sec)")
    for i in range(upper):
        counter.reset()
        t1 = time.time()
        result = fibFunction(n, counter)
        t2 = time.time() - t1
        print("%3d%8d%12s%14.6f" % (n, result, counter, t2))
        n += 1 

def main():
    """Starting point for the profiler app."""
    profileSort(selectionSort, 15)
    profileSort(quickSort, 15)
    profileFib(fib1, 30)
    profileFib(fib2, 30)


if __name__ == "__main__":
    main()

        
        
