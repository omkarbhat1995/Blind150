import pytest
from solution import Solution, ListNode

# --- Helper Functions for Testing ---
def to_linked_list(lst: list) -> ListNode | None:
    """Converts a standard Python list to a linked list."""
    if not lst:
        return None
    dummy = ListNode()
    curr = dummy
    for val in lst:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def to_python_list(head: ListNode | None) -> list:
    """Converts a linked list back to a standard Python list for easy assertion."""
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

# --- Test Suite ---
sol = Solution()

@pytest.mark.parametrize("input_list, expected_list", [
    # Standard Examples
    ([2, 4, 6, 8], [2, 8, 4, 6]),                       # Example 1 (Even length)
    ([2, 4, 6, 8, 10], [2, 10, 4, 8, 6]),               # Example 2 (Odd length)
    
    # Boundary / Small Lengths
    ([1], [1]),                                         # Minimum constraint length
    ([1, 2], [1, 2]),                                   # Two elements (No logical change)
    ([1, 2, 3], [1, 3, 2]),                             # Three elements
    ([1, 2, 3, 4], [1, 4, 2, 3]),                       # Four elements
    
    # Uniform & Palindromic Data (Testing pointer integrity)
    ([5, 5, 5, 5], [5, 5, 5, 5]),                       # All identical elements
    ([1, 2, 1, 2], [1, 2, 2, 1]),                       # Alternating elements
    ([1, 2, 3, 2, 1], [1, 1, 2, 2, 3]),                 # Palindrome array
    
    # Directional / Sequential Extremes
    ([9, 8, 7, 6, 5], [9, 5, 8, 6, 7]),                 # Strictly decreasing
    ([1, 1000], [1, 1000]),                             # Value constraint max difference
    ([1000, 1], [1000, 1]),                             # Reversed max difference
    
    # Medium/Large Iterations
    ([1, 2, 3, 4, 5, 6], [1, 6, 2, 5, 3, 4]),           # Even 6
    ([1, 2, 3, 4, 5, 6, 7], [1, 7, 2, 6, 3, 5, 4]),     # Odd 7
    ([1, 2, 3, 4, 5, 6, 7, 8], [1, 8, 2, 7, 3, 6, 4, 5])# Even 8
])
def test_reorderList(input_list, expected_list):
    """
    Tests the reorderList method against 15 standard, boundary, and edge cases.
    """
    # 1. Convert standard list to Linked List
    head = to_linked_list(input_list)
    
    # 2. Run the solution (mutates in place)
    sol.reorderList(head)
    
    # 3. Convert Linked List back to standard list to verify against expected
    output_list = to_python_list(head)
    
    assert output_list == expected_list