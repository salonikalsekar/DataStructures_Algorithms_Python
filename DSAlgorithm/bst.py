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
            print(curr.data, end=" ")
            self.__preorder(curr.left_child)
            self.__preorder(curr.right_child)

    def inorder(self):
        self.__inorder(self.root)

    def __postorder(self, curr):
        if curr:
            self.__postorder(curr.left_child)
            self.__postorder(curr.right_child)
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


    def delete(self, key):
        self.__delete(key, self.root, None, None)

    def findMinRight(self, curr):
        if curr.left_child:
            return self.findMinRight(curr.left_child)
        else:
            return curr


    def __delete(self, key, curr, prev, is_left):
        if key == curr.data:
            if curr.left_child and curr.right_child:
                minNode =  self.findMinRight(curr.right_child)
                curr.data = minNode.data
                self.__delete(minNode.data, curr.right_child, curr, False)
            if curr.left_child == None and curr.right_child == None:
                if prev:
                    if is_left:
                        prev.left_child = None
                    else:
                        prev.right_child = None
                else:
                    self.root = None
            elif curr.left_child == None:
                if prev:
                    if is_left:
                        prev.left_child = curr.right_child
                    else:
                        prev.right_child = curr.right_child
                else:
                    self.root = curr.right_child

            elif curr.right_child == None:
                if prev:
                    if is_left:
                        prev.left_child = curr.left_child
                    else:
                        prev.right_child = curr.left_child
                else:
                    self.root = curr.left_child

        elif key > curr.data:
            self.__delete(key, curr.right_child, curr, False)
        elif key < curr.data:
            self.__delete(key, curr.left_child, curr, True)

tree = BST()
tree.insert("F")
tree.insert("C")
tree.insert("G")
tree.insert("A")
tree.insert("B")
tree.insert("K")
tree.insert("E")
tree.insert("H")
tree.insert("D")
tree.insert("I")
tree.insert("M")
tree.insert("J")
tree.insert("L")


# tree.inorder()
# tree.preorder()
# tree.postorder()


# tree.search('Z')

tree.inorder()
tree.delete('A')
print('inorder')
tree.inorder()