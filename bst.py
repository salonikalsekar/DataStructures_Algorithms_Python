class Node:
    def __init__(self, key):
        self.data = key
        self.left_child = None
        self.right_child = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not isinstance(key, Node):
            key = Node(key)
        if self.root == None:
            self.root = key
        else:
            self._insert(self.root, key)

    def _insert(self, curr, key):
        if key.data < curr.data:
            if curr.left_child == None:
                curr.left_child = key
            else:
                self._insert(curr.left_child, key)
        elif key.data > curr.data:
            if curr.right_child == None:
                curr.right_child = key
            else:
                self._insert(curr.right_child, key)


tree = BST()

tree.insert('F')
tree.insert('C')
tree.insert('G')
tree.insert('A')
tree.insert('B')
tree.insert('K')
tree.insert('H')

print(tree.root.data)
print(tree.root.left_child.data)
print(tree.root.right_child.data)
print(tree.root.left_child.left_child.data)
print(tree.root.left_child.left_child.right_child.data)
print(tree.root.right_child.data)
print(tree.root.right_child.right_child.data)
print(tree.root.right_child.right_child.left_child.data)
