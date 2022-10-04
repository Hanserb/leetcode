class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Method to display the list
    def printList(self):

        list = []
        cur = self.head

        while cur.next != None:
            list.append(cur.data)
            cur = cur.next
            
        list.append(cur.data)

        print(list)

    # Method to add element to list
    def addToList(self, newData):

        newNode = Node(newData)

        if self.head is None:
            self.head = newNode
            return

        cur = self.head
        while cur.next:
            cur = cur.next

        cur.next = newNode


def mergeLists(l1, l2):

    cur = head = Node()

    while l1 and l2:
        if l1.data < l2.data:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next

    if l1:
        cur.next = l1
    elif l2:
        cur.next = l2

    return head.next


# Create 3 lists
listA = LinkedList()
listB = LinkedList()
listC = LinkedList()


# Add elements to the list in sorted order
listA.addToList(5)
listA.addToList(7)
listA.addToList(10)
listA.addToList(15)

listB.addToList(2)
listB.addToList(3)
listB.addToList(8)
listB.addToList(13)

listA.printList()
listB.printList()

# Call the merge function
listC.head = mergeLists(listA.head, listB.head)

listC.printList()
