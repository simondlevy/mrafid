"""
File: testbag.py
Author: Abrar Al Rafid
A tester program for bag implementations.
"""

from arraybag import ArrayBag
from linkedbag import LinkedBag
from arraysortedbag import ArraySortedBag

# Call the next function as follows:
# test(ArrayBag)
# or
# test(LinkedBag)
# or
# test(ArraySortedBag)

def test(bagType):
    """Expects a bag type as an argument and runs some tests
    on objects of that type."""
    lyst = [2013, 61, 1973]
    print("The list of items added is:", lyst)
    b1 = bagType(lyst)
    print("Length, expect 3:", len(b1))
    print("Expect the bag's string:", b1)
    print("2013 in bag, expect True:", 2013 in b1)
    print("2012 in bag, expect False:", 2012 in b1)
    print("Expect the items on separate lines:")
    for item in b1:
        print(item)
    b1.clear()
    print("Bag cleared, expect {}:", b1)
    b1.add(25)
    b1.remove(25)
    print("Add and remove 25, expect {}:", b1)
    b1 = bagType([1,1,1,2,2])
    b2 = bagType([1,1,2,2,2])

    print("Counting 1 in bag 1, expect 3:", b1.count(1))
    print("Counting 2 in bag 1, expect 2:", b1.count(2))

    print("Testing == with two bags containing 1,1,1,2,2 and 1,1,2,2,2", end = '')
    print(", expect False:", b1 == b2)
    b1 = bagType(lyst)
    b2 = bagType(b1)
    print("Testing == with a clone, expect True:", b1 == b2)
    print("Concatenate with a clone, expect two of each item:", b1 + b2)
    for item in lyst:
        b1.remove(item)
    print("Remove each item, expect {}:", b1)
    print("Crash with index error, or length of " + \
          str(ArrayBag.DEFAULT_CAPACITY * 3))
    for item in range(ArrayBag.DEFAULT_CAPACITY * 3):
        b1.add(item)
    print(len(b1))

def testResize():
    """Tests the resizing of an array-based bag,
    when space is wasted."""
    bag = ArrayBag(range(100))
    print("Added 100 items, length of bag =", len(bag))
    print("Length of array =", len(bag._items))
    for item in range(76):
        bag.remove(item)
    print("Removed 76 items, length of bag =", len(bag))
    print("Length of array =", len(bag._items))
    for item in range(76, 100):
        bag.remove(item)
    print("Removed remaining items, length of bag =", len(bag))
    print("Length of array =", len(bag._items))
    
    

def main():
    """Runs the test functions for bags."""
    test(ArrayBag)
    testResize()
    test(LinkedBag)
    test(ArraySortedBag)

if __name__ == "__main__":
    main()
