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

    def in_order(self):
        # l-root-r
        self._in_order(self.root)
        print()

    def _in_order(self, curr):
        if curr:
            self._in_order(curr.left_child)
            print(curr.data, end=" ")
            self._in_order(curr.right_child)

    def pre_order(self):
        self._pre_order(self.root)
        print()

    def _pre_order(self, curr):
        if curr:
            self._pre_order(curr.left_child)
            self._pre_order(curr.right_child)
            print(curr.data, end = " ")

    def post_order(self):
        self._post_order(self.root)
        print()


    def _post_order(self, curr):
        if curr:
            print(curr.data, end=" ")
            self._post_order(curr.left_child)
            self._post_order(curr.right_child)

    def find_val(self, val):
        return self._find_val(self.root, val)

    def _find_val(self, curr, key):
        if curr:
            if key == curr.data:
                return "Found the value in tree"
            elif key < curr.data:
                return self._find_val(curr.left_child, key)
            else:
                return self._find_val(curr.right_child, key)

        return "not found in the tree"

    def delete_val(self, key):
        return self._delete_val(self.root, None, None, key)

    def _delete_val(self, curr, prev, is_left, key):
        if curr:
            if key == curr.data:
                if curr.left_child == None  and curr.right_child == None:
                    if is_left:
                        prev.left_child = None
                    else:
                        prev.right_child = None
                elif curr.left_child == None:
                    if prev:
                        if is_left:
                            prev.left_child = curr.right_child
                        else:
                            prev.right_child = curr.right_child
                    self.root = curr.right_child
                elif curr.right_child == None:
                    if prev:
                        if is_left:
                            prev.left_child = curr.left_child
                        else:
                            prev.right_child = curr.left_child
                    self.root = curr.left_child

            elif key < curr.data:
                self._delete_val(curr.left_child, curr, True, key)
            elif key> curr.data:
                self._delete_val(curr.right_child, curr, False, key)

        else:
            print(f"{key} not found")



tree = BST()

tree.insert('F')
# tree.insert('C')
tree.insert('C')
tree.in_order()
# delete

tree.delete_val('C')
tree.in_order()

# tree.insert('G')
# tree.insert('A')
# tree.insert('B')
# tree.insert('K')
# tree.insert('H')
# tree.insert('E')
# tree.insert('D')
# tree.insert('I')
# tree.insert('M')
# tree.insert('J')
# tree.insert('L')

# print(tree.root.data)
# print(tree.root.left_child.data)
# print(tree.root.right_child.data)
# print(tree.root.left_child.left_child.data)
# print(tree.root.left_child.left_child.right_child.data)
# print(tree.root.right_child.data)
# print(tree.root.right_child.right_child.data)
# print(tree.root.right_child.right_child.left_child.data)
# tree.insert("H")
# tree.insert("D")
# tree.insert("I")
# tree.insert("M")
# tree.insert("J")
# tree.insert("L")
# tree.insert("F")
# tree.insert("C")
# tree.insert("G")
# tree.insert("A")
# tree.insert("B")
# tree.insert("K")
# tree.insert("E")
#
# tree.pre_order()
#
# tree.post_order()

# print(tree.find_val('E'))
# print(tree.find_val('Z'))

