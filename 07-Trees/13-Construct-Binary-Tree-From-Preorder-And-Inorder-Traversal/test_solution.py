import pytest
from typing import List, Optional
from collections import deque
from solution import Solution, TreeNode

# Helper function to convert a tree back to a LeetCode level-order array list format for assertion checking
def to_level_order(root: Optional[TreeNode]) -> List[Optional[int]]:
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        curr = queue.popleft()
        if curr:
            result.append(curr.val)
            queue.append(curr.left)
            queue.append(curr.right)
        else:
            result.append(None)
            
    # Strip away all trailing None values to mirror LeetCode's structural serialization behavior
    while result and result[-1] is None:
        result.pop()
        
    return result

sol = Solution()

@pytest.mark.parametrize("preorder, inorder, expected", [
    # --- Standard LeetCode Examples ---
    ([1, 2, 3, 4], [2, 1, 3, 4], [1, 2, 3, None, None, None, 4]), # Example 1
    ([1], [1], [1]),                                              # Example 2
    
    # --- Structural Variations ---
    ([3, 9, 20, 15, 7], [9, 3, 15, 20, 7], [3, 9, 20, None, None, 15, 7]), # Classic balanced check
    ([1, 2, 4, 5, 3, 6, 7], [4, 2, 5, 1, 6, 3, 7], [1, 2, 3, 4, 5, 6, 7]), # Full perfect binary tree
    
    # --- Strictly Skewed Structural Formations ---
    ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 2, None, 3, None, 4, None, 5]), # Strictly left-skewed chain linear sequence
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, None, 2, None, 3, None, 4, None, 5]), # Strictly right-skewed chain linear sequence
    
    # --- Zig-Zag Configurations ---
    ([1, 2, 3, 4], [2, 4, 3, 1], [1, 2, None, None, 3, 4]),                # Left-Right zig-zag structural path
    ([1, 2, 3, 4], [1, 3, 4, 2], [1, None, 2, 3, None, None, 4]),          # Right-Left zig-zag structural path
    
    # --- Value Constraint Boundaries ---
    ([-1000], [-1000], [-1000]),                                  # Minimum constraint value bound checking
    ([1000], [1000], [1000]),                                    # Maximum constraint value bound checking
    ([-10, 20, -30], [20, -10, -30], [-10, 20, -30]),              # Explicit negative tracking checks mixed in
    
    # --- Deep Unbalanced Subtree Segments ---
    ([10, 5, 1, 7, 40, 50], [1, 5, 7, 10, 40, 50], [10, 5, 40, 1, 7, None, 50]), # Unbalanced left-branch heavy layout
    ([10, 40, 50, 5, 1, 7], [40, 50, 10, 1, 5, 7], [10, 40, 5, None, 50, 1, 7]), # Complex hybrid cluster
    
    # --- Identical Subtree Values Over Different Structures ---
    ([2, 1, 3, 4], [1, 2, 4, 3], [2, 1, 3, None, None, 4]),        # Right heavy leaf configuration variant
    ([2, 1, 3, 4], [1, 2, 3, 4], [2, 1, 3, None, None, None, 4])   # Alternate right structural layout assignment
])
def test_buildTree(preorder, inorder, expected):
    """
    Validates tree reconstruction output over 15 unique array traversal configurations.
    """
    root = sol.buildTree(preorder, inorder)
    assert to_level_order(root) == expected