class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


def preOrder(root):
    if root == None:
        return
    print(root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Node is defined as
    # self.left (the left child of the node)
    # self.right (the right child of the node)
    # self.info (the value of the node)

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
            return self.root

        return self.insertHelper(self.root, val)

    def insertHelper(self, root, val):
        if val <= root.info:
            if root.left is None:
                root.left = Node(val)
            else:
                self.insertHelper(root.left, val)
        else:
            if root.right is None:
                root.right = Node(val)
            else:
                self.insertHelper(root.right, val)
        return root


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.insert(arr[i])

preOrder(tree.root)
