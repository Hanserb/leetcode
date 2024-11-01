class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        newNode = Node(data)
        currNode = self.head

        while currNode.next:
            currNode = currNode.next

        currNode.next = newNode

    def reverseList(self):
        prev = None
        curr = self.head.next
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head.next = prev

    def display(self) -> None:
        curr_node = self.head

        while curr_node:
            print(curr_node.data, end=" -> ")
            curr_node = curr_node.next
        print("None")


mylist = LinkedList()

mylist.append(1)
mylist.append(2)
mylist.append(3)
mylist.append(4)
mylist.append(5)

mylist.display()

mylist.reverseList()
mylist.display()
