class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f"{self.data}"

class linkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        listPrint = ""
        curr = self.head
        while curr is not None:
            listPrint = listPrint + str(curr.data) + "->"
            curr = curr.next
        if listPrint:
            return "[" + listPrint[:-2] + "]"
        else:
            return "[]"


    def appendValue(self, newData):
        if not isinstance(newData, Node):
            newData = Node(newData)
        if self.head == None:
            self.head = newData
        else:
            self.tail.next = newData
        self.tail = newData


    def addToStart(self, newData):
        if not isinstance(newData, Node):
            newData = Node(newData)
        if self.head == None:
            self.head = newData
        else:
            newData.next = self.head
            self.head = newData

    def length(self):
        count = 0
        while self.head != None:
            self.head = self.head.next
            count += 1
        return count

    def searchValue(self, searchData):
        while self.head != None:
            if self.head.data == searchData:
                return f"Found"
            self.head = self.head.next
        return "not found"

    def deleteElement(self, deldata):
        if self.head == None:
            return "Empty list"
        while self.head != None:
            if self.head.data == deldata:
                self.head = self.head.next
                return "Deleted"
            self.head = self.head.next

        return "Not found"


    def deletestart(self):
        if self.head == None:
            return "none"
        else:
            self.head = self.head.next
            return "Done"

    def deleteEnd(self):
        if self.head == None:
            return "empty"
        else:
            curr = self.head
            while curr.next.next != None:
                curr = curr.next
            curr.next = None
            return "deleted"

    def reverseLinkedList(self, curr, prev):
        if curr is None:
            return "empty"
        elif curr.next == None:
            next = curr.next
            curr.next = prev
            self.head = curr
        else:
            next = curr.next
            curr.next = prev
            self.reverseLinkedList(next, curr)


n1 = Node(1)

linkedlist = linkedList()
linkedlist.appendValue(1)
linkedlist.appendValue(9)
linkedlist.addToStart(8)

# count = linkedlist.length()
print(linkedlist)
#
#
# print(linkedlist.deleteEnd())
# print(linkedlist)

linkedlist.reverseLinkedList(linkedlist.head,None)

print(linkedlist)