"""
Author: Abrar Al Rafid
File: tools.py

A Counter object allows the programmer to create, increment (by 1),
and reset (to 0) a counter.  When a Counter object is printed, its
current value (an integer) is displayed.

The getRandomList function returns a list of random numbers
between 1 and n.
"""

import random

def getRandomList(n):
    """Returns a list of unique random numbers in the
    range 1..n"""
    rand_list = list(range(1, n+1))
    random.shuffle(rand_list)
    return rand_list

# Test function

def testGetRandomList():
    """Prints some random lists."""
    for n in range(1, 10):
        print("n:", n, "List:", getRandomList(n))

def main():
    """Tests the resources."""
    testGetRandomList()

if __name__ == "__main__":
    main()
