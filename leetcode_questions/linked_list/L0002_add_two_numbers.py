# Definition for singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Function to add two numbers represented as linked lists
def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode()
    curr = dummy
    carry = 0

    while l1 or l2 or carry:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0

        # Sum the values and carry
        total = v1 + v2 + carry
        carry = total // 10  # Update carry for next addition
        digit = total % 10  # Current digit to store in node

        # Add new node to result list
        curr.next = ListNode(digit)
        curr = curr.next

        # Move to the next nodes in l1 and l2, if available
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy.next


# Helper function to create a linked list from a list of integers
def create_linked_list(numbers):
    dummy = ListNode()
    current = dummy
    for number in numbers:
        current.next = ListNode(number)
        current = current.next
    return dummy.next


# Helper function to print a linked list
def print_linked_list(head):
    nodes = []
    while head:
        nodes.append(str(head.val))
        head = head.next
    print(" -> ".join(nodes))


# Test Case
# Linked list 1 represents the number 342 (3 -> 4 -> 2)
l1 = create_linked_list([2, 4, 3])
# Linked list 2 represents the number 465 (4 -> 6 -> 5)
l2 = create_linked_list([5, 6, 4])

print("List 1:")
print_linked_list(l1)
print("\nList 2:")
print_linked_list(l2)

# Adding the two numbers
result = add_two_numbers(l1, l2)
print("\nResult:")
print_linked_list(result)
