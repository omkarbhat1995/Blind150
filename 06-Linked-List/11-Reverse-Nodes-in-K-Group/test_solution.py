from typing import Optional

import pytest
from solution import Solution, ListNode

def to_linked_list(arr: list) -> Optional[ListNode]:
    """Converts a standard Python list to a linked list."""
    if not arr:
        return None
    dummy = ListNode()
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def to_python_list(head: Optional[ListNode]) -> list:
    """Converts a linked list back to a standard Python list."""
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

# Initialize the Solution object
sol = Solution()

@pytest.mark.parametrize("input_arr, k, expected", [
    # Standard Examples
    ([1, 2, 3, 4, 5, 6], 3, [3, 2, 1, 6, 5, 4]),     # Example 1: Perfect multiples
    ([1, 2, 3, 4, 5], 3, [3, 2, 1, 4, 5]),           # Example 2: Non-multiple remainder
    
    # Boundary Constraints
    ([1], 1, [1]),                                   # Absolute minimum constraint
    ([1, 2, 3, 4, 5], 1, [1, 2, 3, 4, 5]),           # k = 1 (Should remain completely unchanged)
    ([1, 2, 3, 4, 5], 5, [5, 4, 3, 2, 1]),           # k = n (Reverses the entire list)
    
    # Even and Odd Lengths & Pairings
    ([1, 2], 2, [2, 1]),                             # Small list, k = n
    ([1, 2, 3], 2, [2, 1, 3]),                       # Small list, remainder of 1
    ([10, 20, 30, 40, 50, 60], 2, [20, 10, 40, 30, 60, 50]), # Pairs (k=2) across an even array
    ([1, 2, 3, 4], 3, [3, 2, 1, 4]),                 # Reverses most of the list, leaves 1
    
    # Exactly Halved Lists
    ([1, 2, 3, 4, 5, 6, 7, 8], 4, [4, 3, 2, 1, 8, 7, 6, 5]), # Two equal halves
    
    # Repetitive / Uniform Values
    ([5, 5, 5, 5], 2, [5, 5, 5, 5]),                 # Reversing identical values changes nothing
    ([7, 7, 1, 1, 7, 7], 2, [7, 7, 1, 1, 7, 7]),     # Alternating pairs
    
    # Cascading Remainders
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3, [3, 2, 1, 6, 5, 4, 9, 8, 7, 10]), # Multiple groups, remainder 1
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 4, [4, 3, 2, 1, 8, 7, 6, 5, 9, 10, 11]), # Remainder almost a full group
    
    # Simulated Larger Arrays
    ([i for i in range(1, 21)], 5, [5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 15, 14, 13, 12, 11, 20, 19, 18, 17, 16])
])
def test_reverseKGroup(input_arr, k, expected):
    """
    Tests the reverseKGroup method against 15 standard, boundary, and edge cases.
    """
    # 1. Setup the Linked List
    head = to_linked_list(input_arr)
    
    # 2. Execute Solution
    modified_head = sol.reverseKGroup(head, k)
    
    # 3. Assert by translating back to a standard Python list
    assert to_python_list(modified_head) == expected