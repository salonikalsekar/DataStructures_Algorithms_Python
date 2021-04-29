class Node:
    def __init__(self, key):
        self.left_child = None
        self.right_child = None
        self.data = key


class BST:

    def __init__(self):
        self.root = None

    def insert(self, key):
        if not isinstance(key, Node):
            key = Node(key)
        if not self.root:
            self.root = key
        else:
            self.__insert(self.root, key)


    def __insert(self,curr, key):
        if curr.data < key.data:
            if curr.right_child:
                self.__insert(curr.right_child, key)
            else:
                curr.right_child = key
        else:
            if curr.left_child:
                self.__insert(curr.left_child, key)
            else:
                curr.left_child = key

    def __inorder(self, curr):
        if curr:
            self.__inorder(curr.left_child)
            print(curr.data, end=" ")
            self.__inorder(curr.right_child)

    def preorder(self):
        self.__preorder(self.root)

    def __preorder(self, curr):
        if curr:
            print()
            print(curr.data, end=" ")
            self.__preorder(curr.left_child)
            self.__preorder(curr.right_child)

    def inorder(self):
        self.__postorder(self.root)

    def __postorder(self, curr):
        if curr:
            self.__postorder(curr.left_child)
            self.__postorder(curr.right_child)
            print()
            print(curr.data, end=" ")


    def postorder(self):
        self.__postorder(self.root)

    def search(self, key):
        self.__search(self.root, key)

    def __search(self, curr, key):
        if curr:
            if key == curr.data:
                print('Found')
            elif key < curr.data:
                self.__search(curr.left_child, key)
            else:
                self.__search(curr.right_child, key)
        else:
            print('not found')




tree = BST()
tree.insert("H")
tree.insert("D")
tree.insert("I")
tree.insert("M")
tree.insert("J")
tree.insert("L")
tree.insert("F")
tree.insert("C")
tree.insert("G")
tree.insert("A")
tree.insert("B")
tree.insert("K")
tree.insert("E")


# tree.inorder()
# tree.preorder()
# tree.postorder()


tree.search('Z')