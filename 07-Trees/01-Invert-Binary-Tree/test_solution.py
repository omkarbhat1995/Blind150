import pytest
from collections import deque
from solution import Solution, TreeNode

def build_tree(values: list) -> TreeNode | None:
    """Helper function to build a binary tree from a LeetCode-style level-order list."""
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(values):
        current = queue.popleft()
        
        # Assign left child
        if values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1
        
        # Assign right child
        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1
        
    return root

def to_list(root: TreeNode | None) -> list:
    """Helper function to serialize a binary tree back into a LeetCode-style list."""
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        current = queue.popleft()
        if current:
            result.append(current.val)
            queue.append(current.left)  # type: ignore
            queue.append(current.right)  # type: ignore
        else:
            result.append(None)
            
    # Strip trailing None values to match LeetCode's exact output formatting
    while result and result[-1] is None:
        result.pop()
        
    return result

# Initialize the Solution object
sol = Solution()

@pytest.mark.parametrize("input_list, expected", [
    # Standard LeetCode Examples
    ([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]), # Example 1: Full balanced tree
    ([2, 1, 3], [2, 3, 1]),                         # Example 2: Small balanced tree
    ([], []),                                       # Example 3: Empty tree
    
    # Boundary Constraints
    ([1], [1]),                                     # Single node
    
    # Skewed Trees (Degenerate Trees)
    ([1, 2, None, 3, None, 4], [1, None, 2, None, 3, None, 4]), # Strictly left-skewed
    ([1, None, 2, None, 3], [1, 2, None, 3]),             # Strictly right-skewed
    
    # Negative Numbers (Constraints Check)
    ([-100, -50, -25], [-100, -25, -50]),           # Absolute minimum constraints
    ([-1, None, -2, None, -3], [-1, -2, None, -3]),
    
    # Identical Values
    ([5, 5, 5, 5, 5], [5, 5, 5, None, None, 5, 5]),             # Reversing identicals looks unchanged
    ([1, 1, None], [1, None, 1]),                   # Identical values, uneven structure
    
    # Missing Inner Children
    ([1, 2, 3, None, 4], [1, 3, 2, None, None, 4]), # Left node missing left child
    ([1, 2, 3, 4, None, None, 5], [1, 3, 2, 5, None, None, 4]), 
    
    # Zig-Zag Trees
    ([1, 2, None, None, 3, 4, None], [1, None, 2, 3, None, None, 4]), 
    
    # Disproportionate Depths
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 3, 2, 7, 6, 5, 4, None, None, None, None, None, None, 9, 8]),
    
    # Simulated Larger Tree (Constraint bounds check)
    ([i for i in range(1, 16)], [1, 3, 2, 7, 6, 5, 4, 15, 14, 13, 12, 11, 10, 9, 8])
])
def test_invertTree(input_list, expected):
    """
    Tests the invertTree method against 15 standard, boundary, and edge cases.
    """
    # 1. Setup the Binary Tree
    root = build_tree(input_list)
    
    # 2. Execute Solution
    inverted_root = sol.invertTree(root)
    
    # 3. Assert by translating back to a standard Python list
    assert to_list(inverted_root) == expected