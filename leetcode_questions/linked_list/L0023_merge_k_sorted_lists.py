from typing import List, Optional


# Definition for a singly-linked list node.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # Utility to print the list for easy visualization
    def __str__(self):
        result = []
        current = self
        while current:
            result.append(str(current.val))
            current = current.next
        return " -> ".join(result)


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Edge case: if the list is empty, return None
        if not lists:
            return None

        # We repeatedly merge lists two at a time until we have only one list
        while len(lists) > 1:
            mergedLists = []

            # Process pairs of lists to merge
            for i in range(0, len(lists), 2):
                # Take two lists at a time (or just one if it's the last odd list)
                list1 = lists[i]
                list2 = lists[i + 1] if (i + 1) < len(lists) else None

                # Merge the pair and add the result to mergedLists
                mergedLists.append(self.merge_two_lists(list1, list2))

            # Update lists to the newly merged lists
            lists = mergedLists

        # Return the single merged list
        return lists[0]

    # Helper function to merge two sorted linked lists
    def merge_two_lists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # Initialize a dummy node to build the merged list
        dummy = ListNode()
        current = dummy

        # Merge nodes from both lists in sorted order
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            # Move to the next node in the merged list
            current = current.next

        # Attach any remaining nodes from either list
        current.next = list1 if list1 else list2

        # Return the next node of dummy, which is the head of the merged list
        return dummy.next


# Helper function to build a linked list from a list of values
def build_linked_list(values):
    dummy = ListNode()
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


# Test script for mergeKLists
def test_merge_k_lists():
    # Instantiate Solution
    solution = Solution()

    # Test case: merging three sorted linked lists
    list1 = build_linked_list([1, 4, 5])
    list2 = build_linked_list([1, 3, 4])
    list3 = build_linked_list([2, 6])

    # Put all lists into a list
    lists = [list1, list2, list3]

    # Merge all k lists
    merged_head = solution.mergeKLists(lists)

    # Print the result
    print("Merged linked list:")
    print(merged_head)


# Run the test
test_merge_k_lists()
