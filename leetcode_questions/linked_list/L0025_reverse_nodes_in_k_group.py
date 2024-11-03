from typing import Optional, List


# Definition for singly-linked list node.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # A dummy node to simplify edge cases at the head of the list
        dummy = ListNode(0, head)
        groupPrev = dummy  # Pointer to the previous group's end node (initially points to dummy)

        while True:
            # Find the kth node from the current groupPrev node
            kth = self.getKth(groupPrev, k)
            if not kth:
                # If there's no kth node, we reached the end and can't reverse this group
                break
            groupNext = kth.next  # Pointer to the node after the kth node

            # Reverse the group between groupPrev.next and groupNext
            prev, curr = (
                groupNext,
                groupPrev.next,
            )  # Start the reversal with pointers at group boundaries
            while curr != groupNext:
                tmp = curr.next  # Temporarily store the next node
                curr.next = prev  # Reverse the link direction
                prev = curr  # Move prev to the current node
                curr = tmp  # Move to the next node in the original sequence

            # After reversing, connect the groupPrev node to the new start of this group (kth)
            tmp = (
                groupPrev.next
            )  # Temporarily store the start of this group (to become groupPrev next loop)
            groupPrev.next = kth  # Link previous group to the reversed group
            groupPrev = tmp  # Move groupPrev to the end of the reversed group for the next iteration

        return dummy.next  # The real head is now at dummy.next

    def getKth(self, curr, k):
        # Move `k` nodes ahead or return None if fewer than `k` nodes remain
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr


# Helper function to build a linked list from a list of values
def build_linked_list(values: List[int]) -> Optional[ListNode]:
    dummy = ListNode()
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


# Helper function to print a linked list
def print_linked_list(head: Optional[ListNode]) -> None:
    result = []
    while head:
        result.append(str(head.val))
        head = head.next
    print(" -> ".join(result))


# Testing the reverseKGroup function
if __name__ == "__main__":
    # Create linked list [1, 2, 3, 4, 5]
    head = build_linked_list([1, 2, 3, 4, 5])
    k = 2  # Change this value to test different group sizes

    print("Original list:")
    print_linked_list(head)

    # Initialize Solution and reverse in k-groups
    solution = Solution()
    new_head = solution.reverseKGroup(head, k)

    print("\nReversed in k-groups list:")
    print_linked_list(new_head)
