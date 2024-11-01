# Definition for singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Function to merge two sorted linked lists
def merge_two_lists(list1, list2):
    dummy = ListNode()
    curr = dummy

    while list1 and list2:
        if list1.val < list2.val:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next
        curr = curr.next

    curr.next = list1 if list1 else list2
    return dummy.next


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
list1 = create_linked_list([1, 2, 4])
list2 = create_linked_list([1, 3, 4])

merged_list_head = merge_two_lists(list1, list2)
merged_list = linked_list_to_list(merged_list_head)
print(merged_list)  # Expected output: [1, 1, 2, 3, 4, 4]
