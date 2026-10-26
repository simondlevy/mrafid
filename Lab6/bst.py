"""
bst.py
Abrar Al Rafid
"""

import math


class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def add(self, value):
        if value == self.value:
            return
        if value < self.value:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.add(value)
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.add(value)

    def __contains__(self, value):
        if value == self.value:
            return True
        if value < self.value:
            return self.left is not None and value in self.left
        return self.right is not None and value in self.right

    def __str__(self):
        if self.left is None:
            left = "_"
        else:
            left = str(self.left)

        if self.right is None:
            right = "_"
        else:
            right = str(self.right)

        return f"({self.value} {left} {right})"

    def height(self):
        if self.left is None:
            left_height = -1
        else:
            left_height = self.left.height()

        if self.right is None:
            right_height = -1
        else:
            right_height = self.right.height()

        return 1 + max(left_height, right_height)

    def __len__(self):
        if self.left is None:
            left_size = 0
        else:
            left_size = len(self.left)

        if self.right is None:
            right_size = 0
        else:
            right_size = len(self.right)

        return 1 + left_size + right_size


class BST:

    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.root.add(value)

    def __contains__(self, value):
        return self.root is not None and value in self.root

    def __str__(self):
        if self.root is None:
            return "_"
        else:
            return str(self.root)

    def height(self):
        if self.root is None:
            return -1
        else:
            return self.root.height()

    def __len__(self):
        if self.root is None:
            return 0
        else:
            return len(self.root)

    def isBalanced(self):
        return self.root is None or self.height() < math.ceil(math.log2(len(self)))


def test_bst():
    tree = BST()
    print("Empty tree length:", len(tree), "Expected: 0")
    print("Empty tree height:", tree.height(), "Expected: -1")
    print("Empty tree contains 3:", 3 in tree, "Expected: False")

    for value in [3, 2, 4]:
        tree.add(value)

    print("Tree:", tree, "Expected: (3 (2 _ _) (4 _ _))")
    print("Contains 2:", 2 in tree, "Expected: True")
    print("Contains 3:", 3 in tree, "Expected: True")
    print("Contains 4:", 4 in tree, "Expected: True")
    print("Contains 5:", 5 in tree, "Expected: False")
    print("Length:", len(tree), "Expected: 3")
    print("Height:", tree.height(), "Expected: 1")
    print("Balanced:", tree.isBalanced(), "Expected: True")

    tree.add(3)
    print("Length after adding 3 again:", len(tree), "Expected: 3")

    skinny = BST()
    for value in [2, 3, 4]:
        skinny.add(value)

    print("Skinny tree height:", skinny.height(), "Expected: 2")
    print("Skinny tree balanced:", skinny.isBalanced(), "Expected: False")


if __name__ == "__main__":
    test_bst()
