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

@pytest.mark.parametrize("l1_list, l2_list, expected_list", [
    # Standard Examples
    ([1, 2, 3], [4, 5, 6], [5, 7, 9]),                      # Example 1: No carries
    ([9], [9], [8, 1]),                                     # Example 2: Simple carry
    
    # Zero Cases (Constraints state 0 is valid)
    ([0], [0], [0]),                                        # Absolute zeros
    ([0, 1], [0, 2], [0, 3]),                               # Zero at the head
    ([1, 0, 1], [2, 0, 2], [3, 0, 3]),                      # Interleaved zeros
    
    # Differing Lengths
    ([1, 2], [1, 2, 3], [2, 4, 3]),                         # L2 is longer
    ([1, 2, 3], [1, 2], [2, 4, 3]),                         # L1 is longer
    
    # Complex Carry Chains (Ripple Effect)
    ([9, 9], [1], [0, 0, 1]),                               # L1 cascades into a new decimal place
    ([1], [9, 9, 9, 9], [0, 0, 0, 0, 1]),                   # L2 cascades aggressively
    ([9, 9, 9], [9, 9, 9], [8, 9, 9, 1]),                   # Both cascade into a new place
    
    # Alternating & Stacking Carries
    ([5, 5, 5], [5, 5, 5], [0, 1, 1, 1]),                   # Constant carry generated
    ([2, 8, 2], [8, 2, 8], [0, 1, 1, 1]),                   # Alternating values creating constant carries
    
    # Asymmetric Zeros & Tails
    ([0, 0, 1], [0, 1], [0, 1, 1]),                         # Trailing zeros vs trailing values
    
    # Large Constraint Boundaries (Lists up to 100 nodes)
    ([9] * 50, [1], [0] * 50 + [1]),                        # 50-node carry chain
    ([1] * 100, [2] * 100, [3] * 100)                       # Max length (100) pure addition
])
def test_addTwoNumbers(l1_list, l2_list, expected_list):
    """
    Tests the addTwoNumbers method against 15 standard, boundary, and edge cases.
    """
    # 1. Convert standard lists to Linked Lists
    l1 = to_linked_list(l1_list)
    l2 = to_linked_list(l2_list)
    
    # 2. Run the solution
    result_head = sol.addTwoNumbers(l1, l2)
    
    # 3. Convert Linked List back to standard list to verify against expected
    output_list = to_python_list(result_head)
    
    assert output_list == expected_list