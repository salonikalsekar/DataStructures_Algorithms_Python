class MyDeque:
    """ a double-ended queue implemented using a linked list"""

    class ListItem:
        """ an item in a doubly-linked list"""

        def _init_(self, x, prev, next):
            self.item = x
            self.prev = prev
            self.next = next

    def _init_(self):
        self.head = None
        self.tail = None

    def push_right(self, x):
        if self.head == None:
            self.head = MyDeque.ListItem(x, None, None)
            self.tail = self.head
        else:
            n = MyDeque.ListItem(x, self.tail, None)
            self.tail.next = n
            self.tail = n

    def push_left(self, x):
        if self.head == None:
            self.head = MyDeque.ListItem(x, None, None)
            self.tail = self.head
        else:
            n = MyDeque.ListItem(x, None, self.head)
            self.head.prev = n
            self.head = n

    def pop_left(self):
        if self.head == None:
            return None
        item = self.head.item
        if self.head.next == None:
            self.head = None
            self.tail = None
        else:
            newhead = self.head.next
            newhead.prev = None
            self.head = newhead
        return item

    def pop_right(self):
        item = None

        if self.head == None:
            return None
        else:
            newtail = self.tail.prev
            newtail.next = None
            self.tail = newtail
        # ????
        # ????
        return item

    def print_it(self):
        it = self.head
        print("[[ ", end="")
        while it != None:
            print(it.item, end=" ")
            it = it.next
        print("]]")


Q = MyDeque()
Q.push_right(1)
Q.push_right(2)
Q.push_right(3)
Q.push_left(0)
Q.push_right(4)
Q.print_it()
print("pop_left:", Q.pop_left())
print("pop_right:", Q.pop_right())
Q.print_it()
print("pop_left:", Q.pop_left())
Q.print_it()
print("pop_left:", Q.pop_left())
print("pop_right:", Q.pop_right())
Q.print_it()
print("pop_left:", Q.pop_left())
print("pop_right:", Q.pop_right())