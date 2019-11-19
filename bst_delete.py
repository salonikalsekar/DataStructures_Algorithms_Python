def _delete_val(self, curr, prev, is_left, key):
    if curr:
        if key == curr.data:
            if curr.left_child and curr.right_child:
                min_child = self.min_right_subtree(curr.right_child)
                curr.data = min_child.data
                self._delete_val(curr.right_child, curr, False, min_child.data)
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
            self._delete_val(curr.left_child, curr, True, key)
        elif key > curr.data:
            self._delete_val(curr.right_child, curr, False, key)
    else:
        print(f"{key} not found in Tree")