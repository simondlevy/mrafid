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

    def preorder(self, items):
        # Root -> Left Branch -> Right Branch
        items.append(self.value)
        if self.left is not None:
            self.left.preorder(items)
        if self.right is not None:
            self.right.preorder(items)

    def inorder(self, items):
        # Left Branch -> Root -> Right Branch
        if self.left is not None:
            self.left.inorder(items)
        items.append(self.value)
        if self.right is not None:
            self.right.inorder(items)

    def postorder(self, items):
        # Left Branch -> Right Branch -> Root
        if self.left is not None:
            self.left.postorder(items)
        if self.right is not None:
            self.right.postorder(items)
        items.append(self.value)


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

    def preorder(self):
        items = []
        if self.root is not None:
            self.root.preorder(items)
        return items

    def inorder(self):
        items = []
        if self.root is not None:
            self.root.inorder(items)
        return items

    def postorder(self):
        items = []
        if self.root is not None:
            self.root.postorder(items)
        return items

    def balanced(self):
        items = self.inorder()
        result = BST()

        def recurse(left, right):
            if left <= right:
                midpoint = (left + right) // 2
                result.add(items[midpoint])
                recurse(left, midpoint - 1)
                recurse(midpoint + 1, right)

        recurse(0, len(items) - 1)
        return result


def test_bst():
    tree = BST()
    print("Empty length:", len(tree), "Expected: 0")
    print("Empty height:", tree.height(), "Expected: -1")
    print("Contains 2:", 2 in tree, "Expected: False")
    print("Empty preorder:", tree.preorder(), "Expected: []")
    print("Empty inorder:", tree.inorder(), "Expected: []")
    print("Empty postorder:", tree.postorder(), "Expected: []")
    print("Balanced empty tree:", tree.balanced(), "Expected: _")

    tree.add(2)
    print("One node height:", tree.height(), "Expected: 0")
    tree.add(1)
    tree.add(3)

    print("Tree:", tree, "Expected: (2 (1 _ _) (3 _ _))")
    print("Contains 1:", 1 in tree, "Expected: True")
    print("Contains 4:", 4 in tree, "Expected: False")
    print("Length:", len(tree), "Expected: 3")
    print("Height:", tree.height(), "Expected: 1")
    print("Balanced:", tree.isBalanced(), "Expected: True")
    print("Preorder:", tree.preorder(), "Expected: [2, 1, 3]")
    print("Inorder:", tree.inorder(), "Expected: [1, 2, 3]")
    print("Postorder:", tree.postorder(), "Expected: [1, 3, 2]")
    print("Balance again:", tree.balanced(), "Expected: (2 (1 _ _) (3 _ _))")

    tree.add(2)
    print("Length after duplicate:", len(tree), "Expected: 3")

    skinny = BST()
    for value in [7, 6, 5, 4, 3, 2, 1]:
        skinny.add(value)

    print("Skinny balanced:", skinny.isBalanced(), "Expected: False")
    new_tree = skinny.balanced()
    print("Original height:", skinny.height(), "Expected: 6")
    print("New height:", new_tree.height(), "Expected: 2")
    print("New balanced:", new_tree.isBalanced(), "Expected: True")
    print("New values:", new_tree.inorder(), "Expected: [1, 2, 3, 4, 5, 6, 7]")
    print("New preorder:", new_tree.preorder(), "Expected: [4, 2, 1, 3, 6, 5, 7]")
    print("New postorder:", new_tree.postorder(), "Expected: [1, 3, 2, 5, 7, 6, 4]")

if __name__ == "__main__":
    test_bst()
