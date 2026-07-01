from typing import Dict

class Node:
    """A Node for the Doubly Linked List."""
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    """
    Implements a Least Recently Used (LRU) Cache utilizing 
    a Hash Map and a custom Doubly Linked List for O(1) operations.
    """
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache: Dict[int, Node] = {} # Maps key -> Node
        
        # Dummy nodes to avoid edge cases during pointer reassignment
        self.left = Node(0, 0)  # Least Recently Used indicator
        self.right = Node(0, 0) # Most Recently Used indicator
        self.left.next = self.right # type: ignore
        self.right.prev = self.left # type: ignore

    def remove(self, node: Node) -> None:
        """Removes a node from the doubly linked list."""
        prev_node = node.prev
        nxt_node = node.next
        prev_node.next = nxt_node # type: ignore
        nxt_node.prev = prev_node # type: ignore

    def insert(self, node: Node) -> None:
        """Inserts a node at the rightmost position (Most Recently Used)."""
        prev_node = self.right.prev
        nxt_node = self.right
        
        prev_node.next = node # type: ignore
        nxt_node.prev = node # type: ignore
        node.next = nxt_node # type: ignore
        node.prev = prev_node

    def get(self, key: int) -> int:
        if key in self.cache:
            # Re-insert as the most recently used
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            
        # Create new node and insert as MRU
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        
        # Enforce capacity
        if len(self.cache) > self.cap:
            # The LRU node is always adjacent to the left dummy node
            lru = self.left.next
            self.remove(lru) # type: ignore
            del self.cache[lru.key] # type: ignore