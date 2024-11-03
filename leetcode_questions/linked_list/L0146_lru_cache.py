class Node:
    def __init__(self, key, val):
        self.key = key  # Cache key
        self.val = val  # Cache value
        self.prev = None  # Previous node
        self.next = None  # Next node


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity  # Max capacity of the cache
        self.cache = {}  # Dictionary to store keys and nodes

        # Create dummy nodes for the boundaries of the doubly linked list
        self.left = Node(0, 0)  # Least Recently Used (LRU) boundary
        self.right = Node(0, 0)  # Most Recently Used (MRU) boundary
        self.left.next = self.right  # Initially connect the boundaries
        self.right.prev = self.left

    def remove(self, node):
        # Remove `node` from the doubly linked list
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        # Insert `node` just before the right boundary (most recent position)
        prev, nxt = self.right.prev, self.right
        prev.next = node
        node.prev = prev
        node.next = nxt
        nxt.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            # Move the accessed node to the most recent position
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1  # Key not found

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Remove the existing node to update it
            self.remove(self.cache[key])

        # Add new node to the cache and insert it at the most recent position
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        # If the cache is over capacity, remove the least recently used item
        if len(self.cache) > self.capacity:
            # Remove the LRU node, which is right next to `self.left`
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]  # Delete the LRU node from the hashmap


# Initialize the cache with a capacity of 2
cache = LRUCache(2)

# Test the `put` method
cache.put(1, 1)  # Cache is {1=1}
cache.put(2, 2)  # Cache is {1=1, 2=2}

# Test the `get` method
print(cache.get(1))  # Returns 1, cache is {2=2, 1=1}

# Test `put` method with existing capacity
cache.put(3, 3)  # Removes key 2, adds key 3, cache is {1=1, 3=3}
print(cache.get(2))  # Returns -1 (not found)

cache.put(4, 4)  # Removes key 1, adds key 4, cache is {3=3, 4=4}
print(cache.get(1))  # Returns -1 (not found)
print(cache.get(3))  # Returns 3, cache is {4=4, 3=3}
print(cache.get(4))  # Returns 4, cache is {3=3, 4=4}
