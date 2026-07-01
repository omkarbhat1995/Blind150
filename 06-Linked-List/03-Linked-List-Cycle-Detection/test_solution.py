import pytest
from solution import Solution, ListNode

# --- Helper Functions for Testing ---
def to_linked_list_with_cycle(lst: list, pos: int) -> ListNode | None:
    """
    Converts a standard Python list to a linked list and creates a cycle 
    by connecting the tail to the node at index 'pos'.
    """
    if not lst:
        return None
        
    head = ListNode(lst[0])
    curr = head
    cycle_node = head if pos == 0 else None
    
    for i in range(1, len(lst)):
        curr.next = ListNode(lst[i])
        curr = curr.next
        if i == pos:
            cycle_node = curr
            
    # Connect the tail to the cycle node if pos is valid
    if pos != -1:
        curr.next = cycle_node
        
    return head

# --- Test Suite ---
sol = Solution()

@pytest.mark.parametrize("input_list, pos, expected", [
    # Standard Examples
    ([1, 2, 3, 4], 1, True),                # Example 1
    ([1, 2], -1, False),                    # Example 2
    ([], -1, False),                        # Empty list constraint
    
    # Single Element Boundaries
    ([1], -1, False),                       # Single element, no cycle
    ([1], 0, True),                         # Single element, cycles to itself
    
    # Two Element Boundaries
    ([1, 2], 0, True),                      # Two elements, cycles back to head
    ([1, 2], 1, True),                      # Two elements, cycles to tail (itself)
    
    # Complete Overlaps & Palindromes (Data shouldn't matter, only structure)
    ([5, 5, 5, 5], -1, False),              # Identical elements, no cycle
    ([5, 5, 5, 5], 2, True),                # Identical elements, with cycle
    ([-1, -2, -3, -1], -1, False),          # Negative elements, fake visual cycle, no real cycle
    
    # Complex Cycles in Larger Lists
    ([10, 20, 30, 40, 50, 60], 5, True),    # Cycle on the very last node
    ([10, 20, 30, 40, 50, 60], 0, True),    # Massive cycle back to the absolute head
    ([10, 20, 30, 40, 50, 60], 3, True),    # Cycle directly in the middle
    
    # Extreme Length Constraints
    (list(range(1000)), -1, False),         # Maximum constraints length without cycle
    (list(range(1000)), 499, True),         # Maximum constraints length with massive internal cycle
])
def test_hasCycle(input_list, pos, expected):
    """
    Tests the hasCycle method against 15 standard, boundary, and edge cases.
    """
    # 1. Convert standard list to Linked List with structural cycle
    head = to_linked_list_with_cycle(input_list, pos)
    
    # 2. Run the solution and verify
    assert sol.hasCycle(head) == expected