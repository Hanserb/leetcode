class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

    def delete_node(self, key):
        current_node = self.head

        # If the head node itself holds the key to be deleted
        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return

        # Search for the key to be deleted, keep track of the previous node
        prev = None
        while current_node and current_node.data != key:
            prev = current_node
            current_node = current_node.next

        # If the key was not present in the linked list
        if current_node is None:
            return

        # Unlink the node from the linked list
        prev.next = current_node.next
        current_node = None


# Creating a linked list and adding some nodes
ll = LinkedList()
ll.insert_at_end(1)
ll.insert_at_end(2)
ll.insert_at_end(3)
ll.insert_at_beginning(0)

# Display the linked list
ll.display()  # Output: 0 -> 1 -> 2 -> 3 -> None

# Deleting a node
ll.delete_node(2)

# Display the linked list after deletion
ll.display()  # Output: 0 -> 1 -> 3 -> None
