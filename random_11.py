import math
from math import log


class PriorityQueue():
    import math

    def _init_(self):
        self._array = []

    def push(self, obj):
        # append at end and bubble up
        self._array.append(obj)
        n = len(self._array)
        self._bubble_up(n - 1)

    def pop(self):
        n = len(self._array)
        if n == 0:
            return None
        if n == 1:
            return self._array.pop()

        # replace with last item and sift down:
        obj = self._array[0]
        self._array[0] = self._array.pop()
        self._sift_down(0)
        return obj

    def _parent(self, n):
        return (n - 1) // 2

    def _left_child(self, n):
        return 2 * n + 1

    def _right_child(self, n):
        return 2 * n + 2

    def _bubble_up(self, index):
        while index > 0:
            cur_item = self._array[index]
            parent_idx = self._parent(index)
            parent_item = self._array[parent_idx]

            if cur_item < parent_item:
                # swap with parent
                self._array[parent_idx] = cur_item
                self._array[index] = parent_item
                index = parent_idx
            else:
                break

    def _sift_down(self, index):
        n = len(self._array)

        while index < n:
            cur_item = self._array[index]
            lc = self._left_child(index)
            if n <= lc:
                break

            # first set small child to left child:
            small_child_item = self._array[lc]
            small_child_idx = lc

            # right exists and is smaller?
            rc = self._right_child(index)
            if rc < n:
                r_item = self._array[rc]
                if r_item < small_child_item:
                    # right child is smaller than left child:
                    small_child_item = r_item
                    small_child_idx = rc

            # done: we are smaller than both children:
            if cur_item <= small_child_item:
                break

            # swap with smallest child:
            self._array[index] = small_child_item
            self._array[small_child_idx] = cur_item

            # continue with smallest child:
            index = small_child_idx

    def size(self):
        return len(self._array)

    def is_empty(self):
        return len(self._array) == 0

    def show(self):
        import math

        maxlevels = math.log(len(self._array), 2) + 1
        mxl = math.floor(maxlevels)
        # print(math.floor(maxlevels))

        # a = math.log(4,2)+1
        # b = math.floor(a)
        # print(math.floor(b))

        curlevel = 1
        for i in range(0, len(self._array)):
            if i == 0:
                mylevel = 1
                print((mxl - mylevel) * 2
                "  ", self._array[i])
                curlevel = curlevel + 1

            else:
                ml = math.log(i + 1, 2) + 1
                mylevel = math.floor(ml)
                # print('mylevel is', mylevel)

                if mylevel == curlevel:
                    print((mxl - mylevel) * 2
                    "  ", self._array[i], end = ((mylevel + 1)2)
                    " ")
                    else:
                    print()
                    print((mxl - mylevel) * 2
                    "  ", self._array[i], end = ((mylevel + 1)2)
                    " ")
                    curlevel = curlevel + 1

        h = math.floor(math.log(len(self._array), 2))
        cl = 0
        for i in range(1, len(self._array)):
            nl = math.floor(math.log(i + 1, 2))
            if nl > cl:
                print()
                print((h - nl) * "  ", self._array[i], end=" ")
                cl = cl + 1
            else:
                print((h - cl) * "  ", self._array[i], end=" ")

    def heapify(self, items):
        """ Take an array of unsorted items and replace the contents
        of this priority queue by them. """
        self._array = items
        index = self._parent(len(self._array) - 1)
        for i in range(index, -1, -1):
            self._sift_down(i)

    def decrease_priority(self, old, new):
        """ replace the item old (assumed in the priority queue)
        by the item new, which is assumed to have a smaller value """
        # replace old by new and we can assume that new will compare smaller
        # (so priority is higher or the value is smaller)
        assert (new <= old)
        n = len(self._array)
        for i in range(n):
            if self._array[i] == old:
                self._array[i] = new
                self._bubble_up(i)