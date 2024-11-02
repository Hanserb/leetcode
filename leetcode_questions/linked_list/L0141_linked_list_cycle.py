# Definition for singly-linked list node
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Function to detect a cycle in a linked list
def has_cycle(head: ListNode) -> bool:
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


# Helper function to create a linked list with a cycle for testing
def create_cyclic_list(values, pos):
    head = ListNode(values[0])
    current = head
    cycle_entry = None

    for i in range(1, len(values)):
        new_node = ListNode(values[i])
        current.next = new_node
        current = new_node
        # Mark the cycle entry point
        if i == pos:
            cycle_entry = new_node

    # Link the last node to the cycle entry point to create a cycle
    if cycle_entry:
        current.next = cycle_entry

    return head


# Helper function to create a linked list without a cycle for testing
def create_non_cyclic_list(values):
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


# Test cases
# 1. List with a cycle (1 -> 2 -> 3 -> 4 -> 2 ...)
cyclic_list = create_cyclic_list([1, 2, 3, 4], 1)
print("Cyclic list has cycle:", has_cycle(cyclic_list))  # Expected output: True

# 2. List without a cycle (1 -> 2 -> 3 -> 4)
non_cyclic_list = create_non_cyclic_list([1, 2, 3, 4])
print(
    "Non-cyclic list has cycle:", has_cycle(non_cyclic_list)
)  # Expected output: False
