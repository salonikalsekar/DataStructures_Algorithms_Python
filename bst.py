class Node:
    def __init__(self, key):
        self.left_child = None
        self.right_child = None
        self.data = key


class BST:
    def __init__(self):
        self.root = None

    def __insert(self, curr, key):
        if key.data < curr.data:
            if curr.left_child == None:
                curr.left_child = key
            else:
                self.__insert(curr.left_child, key)
        elif key.data > curr.data:
            if curr.right_child == None:
                curr.right_child = key
            else:
                self.__insert(curr.right_child, key)

    def insert(self, key):
        if not isinstance(key, Node):
            key = Node(key)
        if self.root == None:
            self.root = key

        else:
            self.__insert(self.root, key)

    def inorder(self):
        self.__inorder(self.root)
        print("")

    def __inorder(self, curr):
        if curr:
            self.__inorder(curr.left_child)
            print(curr.data, end=" ")
            self.__inorder(curr.right_child)

    def postorder(self):
        self.__postorder(self.root)
        print("")

    def __postorder(self, curr):
        if curr:
            self.__postorder(curr.left_child)
            self.__postorder(curr.right_child)
            print(curr.data, end = " ")

    def preorder(self):
        self.__preorder(self.root)
        print("")

    def __preorder(self, curr):
        if curr:
            print(curr.data, end=" ")
            self.__preorder(curr.left_child)
            self.__preorder(curr.right_child)


    def findvalue(self, key):
        self.__findvalue(self.root, key)

    def __findvalue(self, curr, key):
        if curr:
            if key == curr.data:
                print("found")
            elif key < curr.data:
                self.__findvalue(curr.left_child, key)
            else:
                self.__findvalue(curr.right_child, key)

        else:
            print("not found")


tree = BST()
tree.insert('F')

print(tree.root.data)
tree.insert('C')
print(tree.root.left_child.data)
tree.insert('G')
tree.insert('A')
tree.insert('B')
tree.insert('K')
tree.insert('H')
tree.insert('E')
tree.insert('D')
tree.insert('I')
tree.insert('M')
tree.insert('J')
tree.insert('L')

tree.inorder()
tree.postorder()
tree.preorder()


tree.findvalue('Z')