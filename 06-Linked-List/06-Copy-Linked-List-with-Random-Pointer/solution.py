from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Optional[Node]' = None, random: 'Optional[Node]' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        Creates a deep copy of a linked list with random pointers using a Hash Map.
        """
        # Map original nodes to their newly created copies. 
        # Including None: None handles edge cases where next/random point to null.
        old_to_copy = {None: None}
        
        # First Pass: Create all the new nodes and map them
        curr = head
        while curr:
            old_to_copy[curr] = Node(curr.val) # type: ignore
            curr = curr.next
            
        # Second Pass: Assign next and random pointers for the copies
        curr = head
        while curr:
            copy = old_to_copy[curr] # type: ignore
            copy.next = old_to_copy[curr.next] # type: ignore
            copy.random = old_to_copy[curr.random] # type: ignore
            curr = curr.next
            
        # Return the head of the new copied list
        return old_to_copy[head] # type: ignore