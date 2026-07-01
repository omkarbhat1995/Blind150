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

@pytest.mark.parametrize("input_list, k, expected", [
    # --- Standard LeetCode Examples ---
    ([2, 1, 3], 1, 1),                                    # Example 1: Smallest element in balanced tree
    ([4, 3, 5, 2, None], 4, 5),                           # Example 2: Target is the max value in the tree
    
    # --- Single Element & Minimum Constraints ---
    ([0], 1, 0),                                          # Single node, value 0 (minimum constraint value)
    ([1000], 1, 1000),                                    # Single node, value 1000 (maximum constraint value)
    
    # --- Target Position Variants (Smallest vs Largest) ---
    ([3, 1, 4, None, 2], 1, 1),                           # Target is the absolute minimum node
    ([3, 1, 4, None, 2], 4, 4),                           # Target is the absolute maximum node
    ([3, 1, 4, None, 2], 2, 2),                           # Target is a deeply nested middle child node
    
    # --- Strictly Skewed Linear Formations ---
    ([1, None, 2, None, 3, None, 4, None, 5], 3, 3),      # Right-skewed linear line path (finding the median)
    ([1, None, 2, None, 3, None, 4, None, 5], 5, 5),      # Right-skewed linear line path (finding the leaf)
    ([5, 4, None, 3, None, 2, None, 1], 1, 1),            # Left-skewed linear line path (deep leaf check)
    ([5, 4, None, 3, None, 2, None, 1], 4, 4),            # Left-skewed linear line path (internal element check)
    
    # --- Unbalanced Structurally Incomplete Paths ---
    ([5, 2, 6, None, 4, None, 7, 3], 2, 3),               # Deeply buried left child on a right branch
    ([20, 10, 30, 5, 15, None, 35, None, None, 12], 3, 12), # Multi-level branch seeking value 12
    
    # --- Complete Large Balanced BST ---
    ([50, 25, 75, 12, 37, 62, 87], 1, 12),                # First element of a fully populated tree
    ([50, 25, 75, 12, 37, 62, 87], 7, 87),                # Last element of a fully populated tree
    ([50, 25, 75, 12, 37, 62, 87], 4, 50)                 # Exact structural root element (median value)
])
def test_kthSmallest(input_list, k, expected):
    """
    Validates the kthSmallest solution across 15+ edge, boundary, and balanced scenarios.
    """
    root = build_tree(input_list)
    assert sol.kthSmallest(root, k) == expected