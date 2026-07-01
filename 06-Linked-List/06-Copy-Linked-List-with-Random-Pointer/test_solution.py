import pytest
from solution import Solution, Node

# --- Helper Functions for Testing ---
def to_linked_list_with_random(lst: list) -> Node | None:
    """Converts a standard Python list of [val, random_index] to a custom Node list."""
    if not lst:
        return None
        
    # Create all nodes first
    nodes = [Node(val) for val, _ in lst]
    
    # Assign next and random pointers
    for i, (val, rand_idx) in enumerate(lst):
        if i < len(nodes) - 1:
            nodes[i].next = nodes[i + 1]
        if rand_idx is not None:
            nodes[i].random = nodes[rand_idx]
            
    return nodes[0]

def to_python_list(head: Node | None) -> list:
    """Converts a custom Node list back to a standard Python list of [val, random_index]."""
    if not head:
        return []
        
    # First pass: map each node to its index
    node_to_idx = {}
    curr = head
    idx = 0
    while curr:
        node_to_idx[curr] = idx
        curr = curr.next
        idx += 1
        
    # Second pass: build the result list
    res = []
    curr = head
    while curr:
        rand_idx = node_to_idx.get(curr.random, None)
        res.append([curr.val, rand_idx])
        curr = curr.next
        
    return res

# --- Test Suite ---
sol = Solution()

@pytest.mark.parametrize("input_list", [
    # Standard Examples
    [[3, None], [7, 3], [4, 0], [5, 1]],            # Example 1
    [[1, None], [2, 2], [3, 2]],                    # Example 2
    [],                                             # Empty List
    
    # Boundary & Small Lists
    [[1, None]],                                    # Single element, random is null
    [[1, 0]],                                       # Single element, random points to itself
    [[1, 1], [2, 0]],                               # Two elements, criss-cross random pointers
    
    # Random Pointer Edge Cases
    [[1, None], [2, None], [3, None]],              # All random pointers are null
    [[1, 0], [2, 0], [3, 0]],                       # All random pointers point to the head
    [[1, 2], [2, 2], [3, 2]],                       # All random pointers point to the tail
    [[1, 0], [2, 1], [3, 2], [4, 3]],               # All random pointers point to themselves
    
    # Value Edge Cases (Constraints: -100 to 100)
    [[5, 2], [5, 0], [5, 1]],                       # Identical values, mixed randoms
    [[-100, 1], [100, 0]],                          # Maximum constraint boundaries
    [[-50, 2], [0, None], [50, 0]],                 # Mixed negative, zero, and positive
    
    # Larger Lists & Cycles
    [[i, (i - 1) if i > 0 else None] for i in range(10)], # 10 elements, random points to previous
    [[i, (i + 1) % 15] for i in range(15)]                # 15 elements, random points to next (circular)
])
def test_copyRandomList(input_list):
    """
    Tests the copyRandomList method against 15 standard, boundary, and edge cases.
    Verifies both structural integrity and Deep Copy memory isolation.
    """
    # 1. Convert standard list to our original Linked List
    original_head = to_linked_list_with_random(input_list)
    
    # 2. Run the solution to get the copied list
    copied_head = sol.copyRandomList(original_head)
    
    # 3. Verify Memory Independence (The "Deep" part of Deep Copy)
    curr_orig = original_head
    curr_copy = copied_head
    while curr_orig and curr_copy:
        # The objects MUST occupy different memory addresses
        assert curr_orig is not curr_copy, "Deep copy failed: Node memory references are identical."
        curr_orig = curr_orig.next
        curr_copy = curr_copy.next
        
    # 4. Verify Structural and Value Integrity
    output_list = to_python_list(copied_head)
    assert output_list == input_list