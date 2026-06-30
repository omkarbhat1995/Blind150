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

@pytest.mark.parametrize("input_list, n, expected_list", [
    # Standard Examples
    ([1, 2, 3, 4], 2, [1, 2, 4]),                       # Example 1: Remove from middle
    ([5], 1, []),                                       # Example 2: Remove single element
    ([1, 2], 2, [2]),                                   # Example 3: Remove head of size 2
    
    # Boundary Removals (Head and Tail)
    ([1, 2, 3, 4, 5], 5, [2, 3, 4, 5]),                 # Remove absolute head
    ([1, 2, 3, 4, 5], 1, [1, 2, 3, 4]),                 # Remove absolute tail
    
    # Small Lists Edge Cases
    ([1, 2], 1, [1]),                                   # Remove tail of size 2
    ([10, 20, 30], 2, [10, 30]),                        # Remove exact middle of size 3
    
    # Uniform / Duplicate Data
    ([5, 5, 5, 5], 2, [5, 5, 5]),                       # Identical elements
    ([0, 0, 0], 3, [0, 0]),                             # Lower constraint value (0), remove head
    ([100, 100], 1, [100]),                             # Upper constraint value (100)
    
    # Large List (Approaching Max Constraint sz = 30)
    (list(range(30)), 15, list(range(15)) + list(range(16, 30))), # Remove middle in max list
    (list(range(30)), 30, list(range(1, 30))),                    # Remove head in max list
    (list(range(30)), 1, list(range(29))),                        # Remove tail in max list
    
    # Value Parity & Patterns
    ([1, 3, 5, 7, 9], 4, [1, 5, 7, 9]),                 # Only odd numbers, n=4
    ([2, 4, 6, 8, 10], 3, [2, 4, 8, 10])                # Only even numbers, n=3
])
def test_removeNthFromEnd(input_list, n, expected_list):
    """
    Tests the removeNthFromEnd method against 15 standard, boundary, and edge cases.
    """
    # 1. Convert standard list to Linked List
    head = to_linked_list(input_list)
    
    # 2. Run the solution
    modified_head = sol.removeNthFromEnd(head, n)
    
    # 3. Convert Linked List back to standard list to verify against expected
    output_list = to_python_list(modified_head)
    
    assert output_list == expected_list