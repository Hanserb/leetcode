# Definition for a Node in a linked list
class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


# Function to copy a linked list with next and random pointers
def copyRandomList(head: "Node") -> "Node":
    if not head:
        return None  # Return None if the input list is empty

    # Dictionary to map original nodes to their copies
    oldToCopy = {None: None}

    # First pass: create copies of each node and map them
    curr = head
    while curr:
        # Create a copy of the current node
        copy = Node(curr.val)
        # Map the original node to its copy
        oldToCopy[curr] = copy
        # Move to the next node
        curr = curr.next

    # Second pass: assign next and random pointers for each copied node
    curr = head
    while curr:
        copy = oldToCopy[curr]  # Get the copy of the current node
        copy.next = oldToCopy[curr.next]  # Set the next pointer
        copy.random = oldToCopy[curr.random]  # Set the random pointer
        curr = curr.next  # Move to the next node

    # Return the head of the copied linked list
    return oldToCopy[head]


# Helper function to create a linked list with random pointers from a list of values and random indices
def create_linked_list(values, random_indices):
    nodes = [Node(val) for val in values]
    for i, node in enumerate(nodes):
        if i + 1 < len(nodes):
            node.next = nodes[i + 1]
        if random_indices[i] is not None:
            node.random = nodes[random_indices[i]]
    return nodes[0] if nodes else None


# Helper function to print a linked list with next and random pointers
def print_linked_list(head):
    nodes = []
    curr = head
    while curr:
        random_val = curr.random.val if curr.random else None
        nodes.append(f"[Val: {curr.val}, Random: {random_val}]")
        curr = curr.next
    print(" -> ".join(nodes))


# Example Usage
# Creating a linked list: 1 -> 2 -> 3
# Random pointers: 1's random points to 3, 2's random points to 1, 3's random points to 2
values = [1, 2, 3]
random_indices = [
    2,
    0,
    1,
]  # Defines which index each node's random pointer should point to

original_head = create_linked_list(values, random_indices)
print("Original List:")
print_linked_list(original_head)

# Copy the list with random pointers
copied_head = copyRandomList(original_head)
print("\nCopied List:")
print_linked_list(copied_head)
