class Node:
    def __init__(self, value: int):
        self.value = value
        self.next: Node | None = None


class LinkedList:
    def __init__(self):
        self.head: Node | None = None

    def insert_at_head(self, value: int) -> None:
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_at_tail(self, value: int) -> None:
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return

        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next
        cur_node.next = new_node

    def reverse_list(self) -> None:
        curr_node = self.head
        prev_node: Node | None = None

        while curr_node:
            nxt = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = nxt
        self.head = prev_node

    def print_list(self) -> None:
        curr_node = self.head
        while curr_node:
            print(curr_node.value, end=" -> ")
            curr_node = curr_node.next
        print("None")


if __name__ == "__main__":
    my_linked_list = LinkedList()

    my_linked_list.insert_at_head(5)
    my_linked_list.insert_at_head(4)
    my_linked_list.insert_at_head(3)

    my_linked_list.insert_at_tail(12)
    my_linked_list.insert_at_tail(15)
    my_linked_list.insert_at_tail(18)
    my_linked_list.insert_at_tail(21)

    my_linked_list.print_list()

    my_linked_list.reverse_list()

    my_linked_list.print_list()
