import pytest
from solution import Solution, ListNode

# --- Helper Functions for Testing ---
def to_linked_list(lst: list) -> ListNode | None:
    """Converts a standard Python list to a linked list."""
    dummy = ListNode()
    curr = dummy
    for val in lst:
        curr.next = ListNode(val)
        curr = curr = curr.next
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
    ([0, 1, 2, 3], [3, 2, 1, 0]),               # Example 1
    ([], []),                                   # Example 2 (Empty List)
    
    # Small / Single Element Boundary
    ([1], [1]),                                 # Single element
    ([1, 2], [2, 1]),                           # Two elements
    
    # Uniform Elements
    ([5, 5, 5, 5], [5, 5, 5, 5]),               # All identical elements
    ([0, 0, 0], [0, 0, 0]),                     # All zeros
    
    # Negative Numbers & Mixed Parity
    ([-1, -2, -3, -4], [-4, -3, -2, -1]),       # Purely negative
    ([-1, 2, -3, 4], [4, -3, 2, -1]),           # Alternating signs
    
    # Palindromes (Reversal shouldn't change output logically)
    ([1, 2, 1], [1, 2, 1]),                     # Odd length palindrome
    ([1, 2, 2, 1], [1, 2, 2, 1]),               # Even length palindrome
    
    # Constraint Boundaries 
    ([1000, 500, 0], [0, 500, 1000]),           # Upper constraint limits
    ([-1000, -500, 0], [0, -500, -1000]),       # Lower constraint limits
    ([1000, -1000], [-1000, 1000]),             # Extreme jump
    
    # Large Range Arrays
    (list(range(50)), list(range(49, -1, -1))), # 50 incrementally increasing elements
    (list(range(50, 0, -1)), list(range(1, 51)))# 50 incrementally decreasing elements
])
def test_reverseList(input_list, expected_list):
    """
    Tests the reverseList method against 15 standard, boundary, and edge cases.
    """
    # 1. Convert standard list to Linked List
    head = to_linked_list(input_list)
    
    # 2. Run the solution
    reversed_head = sol.reverseList(head)
    
    # 3. Convert Linked List back to standard list to verify against expected
    output_list = to_python_list(reversed_head)
    
    assert output_list == expected_list