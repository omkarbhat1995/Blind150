import pytest
from solution import Solution, ListNode

def to_linked_list(arr: list) -> ListNode | None:
    """Helper function to convert a standard Python list to a linked list."""
    if not arr:
        return None
    dummy = ListNode()
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def to_python_list(head: ListNode | None) -> list:
    """Helper function to convert a linked list back to a standard Python list."""
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

# Initialize the Solution object
sol = Solution()

@pytest.mark.parametrize("input_lists, expected", [
    # Standard Examples
    ([[1, 2, 4], [1, 3, 5], [3, 6]], [1, 1, 2, 3, 3, 4, 5, 6]),
    ([], []),
    ([[]], []),
    
    # Boundary & Empty List Variants
    ([[], [], []], []),                                         # Multiple empty lists
    ([[1, 2, 3]], [1, 2, 3]),                                   # Single list
    ([[1], [2, 3, 4], [0, 5]], [0, 1, 2, 3, 4, 5]),             # Highly varying lengths
    
    # Negative Numbers & Constraints
    ([[-5, -1, 5], [-10, 0, 10]], [-10, -5, -1, 0, 5, 10]),     # Standard negative ranges
    ([[-1000, 1000], [-500, 500]], [-1000, -500, 500, 1000]),   # Absolute min/max boundaries
    
    # Repetition & Ties
    ([[2, 2], [2], [2, 2, 2]], [2, 2, 2, 2, 2, 2]),             # All identical elements
    ([[0, 1], [0, 2], [0, 3]], [0, 0, 0, 1, 2, 3]),             # Duplicate minimums across lists
    
    # Sequence Extremes
    ([[1, 2], [3, 4], [5, 6]], [1, 2, 3, 4, 5, 6]),             # Perfectly sequential chunks
    ([[5, 6], [3, 4], [1, 2]], [1, 2, 3, 4, 5, 6]),             # Reverse sequential chunks
    ([[1, 4, 7], [2, 5, 8], [3, 6, 9]], [1, 2, 3, 4, 5, 6, 7, 8, 9]), # Perfectly interleaved
    
    # Disproportionate Lengths
    ([[1, 100], [2, 3, 4, 5, 6, 7]], [1, 2, 3, 4, 5, 6, 7, 100]), # One massive outlier
    
    # Large K Mock (Constraint boundary check)
    ([[1]] * 100, [1] * 100)                                    # 100 individual lists of size 1
])
def test_mergeKLists(input_lists, expected):
    """
    Tests the mergeKLists method against 15 standard, boundary, and edge cases.
    """
    # 1. Convert lists of arrays into lists of Linked Lists
    linked_lists = [to_linked_list(arr) for arr in input_lists]
    
    # 2. Execute solution
    merged_head = sol.mergeKLists(linked_lists)
    
    # 3. Assert by translating back to a standard python list
    assert to_python_list(merged_head) == expected