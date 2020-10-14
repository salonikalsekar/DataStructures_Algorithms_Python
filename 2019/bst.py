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


    def min_subtree_right(self, curr):
        print("testing")
        print(curr.data)
        if curr.left_child == None:
            return curr
        else:
            return self.min_subtree_right(curr.left_child)


    def delete(self, key):
        self._delete(self.root, None, None, key)

    def _delete(self, curr, prev, is_left,  key):

        if curr:
            if curr.data == key:
                if curr.left_child and curr.right_child:
                    min_child = self.min_subtree_right(curr.right_child)
                    curr.data = min_child.data
                    self._delete(curr.right_child, curr, False, min_child.data)
                elif curr.left_child == None and curr.right_child == None:
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

                else:
                    if prev:
                        if is_left:
                            prev.left_child = curr.left_child
                        else:
                            prev.right_child = curr.left_child
                    else:
                        self.root = curr.left_child

            elif key < curr.data:
                self._delete(curr.left_child, curr, True,  key)
            elif key>curr.data:
                self._delete(curr.right_child, curr, False,  key)

        else:
            print("key not found")

tree = BST()
tree.insert('F')

# print(tree.root.data)
tree.insert('C')
# print(tree.root.left_child.data)
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
print(tree.inorder())
tree.delete('K')
print(tree.inorder())
# tree.inorder()
# tree.postorder()
# tree.preorder()

# tree.findvalue('Z')


