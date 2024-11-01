# Definition for singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Function to remove the N-th node from the end of the list
def remove_nth_from_end(head, n):
    # Create a dummy node that points to the head of the list
    # This helps handle cases where we might need to remove the first node
    dummy = ListNode(0, head)
    left_pointer = dummy
    right_pointer = head

    # Move the right pointer `n` steps forward in the list
    for _ in range(n):
        if right_pointer:
            right_pointer = right_pointer.next

    # Move both pointers forward until right_pointer reaches the end
    # At this point, left_pointer will be just before the node we need to remove
    while right_pointer:
        left_pointer = left_pointer.next
        right_pointer = right_pointer.next

    # Skip the N-th node from the end by changing the next pointer of left_pointer
    left_pointer.next = left_pointer.next.next

    # Return the head of the modified list
    return dummy.next


# Helper functions to create and print linked lists for easy testing
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
n = 2
new_head = remove_nth_from_end(head, n)
print(linked_list_to_list(new_head))  # Expected output: [1, 2, 3, 5]
