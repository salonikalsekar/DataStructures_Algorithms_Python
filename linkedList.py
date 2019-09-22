class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return f"{self.data}"

class LinkedList:
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

    def length(self):
        count = 0
        while self.head != None:
            self.head =self.head.next
            count += 1
        return count

    def addTostart(self, newNode):
        if not isinstance(newNode, Node):
            newNode = Node(newNode)
        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode


    def searchValue(self, data):

        if self.head == None:
            return "Empty"
        while self.head != None:
            if self.head.data == data:
                return "Found"
            self.head = self.head.next
        return "Not found"


    # def deleteElement(self, data):
    #     if self.head == None:
    #         return "Empty list"
    #     while self.head != None:
    #         self.head = self.head.next
    #         if self.head.data == data:
    #             self.head = self.head.next
    #             return "Deleted"
    #     return "Not found"

    def deleteStartElement(self):
        if self.head == None:
            return "Empty list"
        else:
            self.head = self.head.next
            return "Done"

    # def deleteLastElement(self):
    #     if self.head == None:
    #         return "Empty list"
    #     while self.head.next.next != None:
    #         self.head = self.head.next
    #     print(self.head.next)
    #     self.head.next = None
    #     return "deleted"

    ############################################REVERSE LINKED LIST########################################
    def reverseLinkedList(self, current, previous):
        if self.head is None:
            return "Empty list"

        elif current.next is None:
            next = current.next
            current.next = previous
            self.head = current

        else:
            next = current.next
            current.next = previous
            self.reverseLinkedList(next, current)


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)


mylist = LinkedList()

mylist.appendValue(node1)
mylist.appendValue(node2)
mylist.appendValue(node3)
mylist.appendValue(node4)
mylist.appendValue(node5)

# print(mylist)

# count the number of elements in the linkedlist
# count = mylist.length()
# print(count)

# add a new element in the beginning of the linked list
# mylist.addTostart(90)
# print(mylist)

# search an element
# print(mylist.searchValue(66))

# print(mylist.deleteElement(4))
# print(mylist)

# print(mylist.deleteStartElement())
# print(mylist)

# print(mylist.deleteLastElement())
# print(mylist)




mylist.reverseLinkedList(mylist.head, None)
print(mylist)