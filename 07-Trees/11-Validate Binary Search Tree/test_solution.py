import pytest
from typing import List, Optional
from collections import deque
from solution import Solution, TreeNode

# Helper function to construct a level-order binary tree from a list representation
def build_tree(nodes: List[Optional[int]]) -> Optional[TreeNode]:
    if not nodes or nodes[0] is None:
        return None
    
    root = TreeNode(nodes[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(nodes):
        curr = queue.popleft()
        
        # Assign Left Child
        if i < len(nodes) and nodes[i] is not None:
            curr.left = TreeNode(nodes[i])
            queue.append(curr.left)
        i += 1
        
        # Assign Right Child
        if i < len(nodes) and nodes[i] is not None:
            curr.right = TreeNode(nodes[i])
            queue.append(curr.right)
        i += 1
        
    return root

sol = Solution()

@pytest.mark.parametrize("input_list, expected", [
    # --- Standard LeetCode Examples ---
    ([2, 1, 3], True),                               # Example 1: Balanced and valid
    ([1, 2, 3], False),                              # Example 2: Invalid left child > root
    
    # --- Structural Variations ---
    ([5, 1, 4, None, None, 3, 6], False),            # Tricky Case: 3 is on the right of 5, but left of 4 (Invalid)
    ([10, 5, 15, None, None, 6, 20], False),         # Tricky Case: 6 is in right subtree of 10 (Invalid)
    ([10, 5, 15, None, None, 12, 20], True),         # Valid variant of the above sneaky boundary check
    
    # --- Single Element & Minimum Constraints ---
    ([0], True),                                     # Minimum size tree (1 node)
    ([-1000], True),                                 # Constraint Boundary: Minimum value
    ([1000], True),                                  # Constraint Boundary: Maximum value
    
    # --- Duplicate Values (Strict Inequality Check) ---
    ([1, 1], False),                                 # Left duplicate (BST requires strictly less than)
    ([1, None, 1], False),                           # Right duplicate (BST requires strictly greater than)
    ([10, 5, 15, 5, None, None, None], False),       # Duplicate value deeper down the tree
    
    # --- Skewed Tree Lines ---
    ([1, None, 2, None, 3, None, 4], True),          # Strictly right-skewed valid line
    ([4, 3, None, 2, None, 1], True),                # Strictly left-skewed valid line
    ([1, None, 2, None, 0], False),                  # Right-skewed chain containing an invalid lower boundary violation
    
    # --- Larger Complex Balanced Valid BST ---
    ([50, 30, 70, 20, 40, 60, 80], True)             # Fully balanced multi-level complete valid BST
])
def test_isValidBST(input_list, expected):
    """
    Validates the solution against 15 test cases ensuring robust edge-case tracking.
    """
    root = build_tree(input_list)
    assert sol.isValidBST(root) == expected