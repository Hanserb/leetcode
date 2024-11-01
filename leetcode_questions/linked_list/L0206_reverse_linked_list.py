# Definition for singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Function to reverse a linked list
def reverse_list(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev


# Helper functions to create and convert lists for testing
def create_linked_list(arr):
    dummy = ListNode()
    curr = dummy
    for num in arr:
        curr.next = ListNode(num)
        curr = curr.next
    return dummy.next


def linked_list_to_list(head):
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    return arr


# Test case
head = create_linked_list([1, 2, 3, 4, 5])
reversed_head = reverse_list(head)
reversed_list = linked_list_to_list(reversed_head)
print(reversed_list)  # Expected output: [5, 4, 3, 2, 1]
