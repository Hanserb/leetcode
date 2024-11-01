# Definition for singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Function to reorder list
def reorder_list(head):
    if not head or not head.next:
        return  # No reordering needed for an empty list or single node

    # Step 1: Find the middle of the list using slow and fast pointers
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse the second half of the list
    second_half = slow.next
    slow.next = None  # Split the list into two halves
    prev = None
    while second_half:
        next_node = second_half.next
        second_half.next = prev  # Reverse pointer direction
        prev = second_half
        second_half = next_node

    # Step 3: Merge the two halves
    first_half, second_half = head, prev  # prev is the head of the reversed second half
    while second_half:
        # Save the next nodes
        tmp1, tmp2 = first_half.next, second_half.next
        # Interleave nodes
        first_half.next = second_half
        second_half.next = tmp1
        # Move to the next nodes
        first_half, second_half = tmp1, tmp2


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
reorder_list(head)
print(linked_list_to_list(head))  # Expected output: [1, 5, 2, 4, 3]
