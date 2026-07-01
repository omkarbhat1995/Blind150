import pytest
from solution import Solution, ListNode

# --- Helper Functions for Testing ---
def to_linked_list(lst: list) -> ListNode | None:
    """Converts a standard Python list to a linked list."""
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

@pytest.mark.parametrize("l1, l2, expected", [
    # Standard Examples
    ([1, 2, 4], [1, 3, 5], [1, 1, 2, 3, 4, 5]), # Example 1
    ([], [1, 2], [1, 2]),                       # Example 2 (One empty)
    ([], [], []),                               # Example 3 (Both empty)
    
    # Differing Lengths
    ([1, 2, 3, 4, 5], [6, 7], [1, 2, 3, 4, 5, 6, 7]), # List 1 is longer
    ([1, 2], [3, 4, 5, 6], [1, 2, 3, 4, 5, 6]),       # List 2 is longer
    
    # Complete Overlaps (One list strictly smaller/larger)
    ([1, 2, 3], [4, 5, 6], [1, 2, 3, 4, 5, 6]), # List 1 strictly smaller
    ([7, 8, 9], [1, 2, 3], [1, 2, 3, 7, 8, 9]), # List 2 strictly smaller
    
    # Interleaved & Duplicates
    ([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]), # Perfectly interleaved
    ([1, 1, 1], [1, 1, 1], [1, 1, 1, 1, 1, 1]), # All identical duplicates
    ([2, 2, 4], [2, 4, 4], [2, 2, 2, 4, 4, 4]), # Mixed duplicates
    
    # Negative Numbers & Zero
    ([-5, -2, 0], [-3, 1, 4], [-5, -3, -2, 0, 1, 4]), # Mixed negatives and zero
    ([-10, -5], [-15, -1], [-15, -10, -5, -1]),       # Strictly negative lists
    
    # Boundary Constraints
    ([-100], [100], [-100, 100]),                     # Extreme constraint limits
    ([100], [-100], [-100, 100]),                     # Extreme constraint limits swapped
    ([-100, 100], [-100, 100], [-100, -100, 100, 100])# Multiple constraint limits
])
def test_mergeTwoLists(l1, l2, expected):
    """
    Tests the mergeTwoLists method against 15 standard, boundary, and edge cases.
    """
    # 1. Convert standard lists to Linked Lists
    head1 = to_linked_list(l1)
    head2 = to_linked_list(l2)
    
    # 2. Run the solution
    merged_head = sol.mergeTwoLists(head1, head2)
    
    # 3. Convert resulting Linked List back to standard list to verify against expected
    output_list = to_python_list(merged_head)
    
    assert output_list == expected