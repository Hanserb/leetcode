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


def mergeTwoLists(self, list1, list2):
    pass

if __name__ == "__main__":
    list_1 = LinkedList()
    list_1.insert_at_head(1)
    list_1.insert_at_head(2)
    list_1.insert_at_head(4)

    list_2 = LinkedList()
    list_2.insert_at_head(1)
    list_2.insert_at_head(3)
    list_2.insert_at_head(4)

    list_1.print_list()
    list_2.print_list()

    mergeTwoLists(list_1, list_2)
