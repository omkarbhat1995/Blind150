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
    ([1, 2, 3], 6),                                           # Example 1: 2 -> 1 -> 3
    ([-15, 10, 20, None, None, 15, 5, -5], 40),               # Example 2: 15 -> 20 -> 5
    
    # --- Single Element & Minimum Boundary Constraints ---
    ([0], 0),                                                 # Single root with zero value
    ([-1000], -1000),                                         # Constraint Bound: Single absolute minimum value
    ([1000], 1000),                                           # Constraint Bound: Single absolute maximum value
    
    # --- All Negative Tree Structures ---
    ([-3], -3),                                               # Negative single node 
    ([-10, -5, -20], -5),                                     # All negative nodes (must pick the largest single node value)
    ([-2, -1, None, -3], -1),                                 # Skewed negative layout picking the max single node
    
    # --- Subtree Dominance (Path doesn't go through root) ---
    ([-10, 20, 30, None, None, 15, 7], 55),                   # Path 15 -> 30 -> 7 entirely within the right subtree
    ([5, -20, -30, 15, 10, None, None], 15),                  # Path 15 -> -20 -> 10 doesn't happen; max path is 15 -> -20 -> 10? No, 15+10 = 25 is best.
    
    # --- Skewed Linear Formations (Pruning negative ends) ---
    ([1, None, 2, None, 3, None, -5], 6),                     # Right-skewed line pruning a negative leaf node
    ([1, None, -2, None, 3, None, 4], 7),                     # Intermittent negative node splitting the path (3 -> 4 is better than 1 -> -2 -> 3 -> 4)
    ([4, -1, None, 5, None, -2], 8),                          # Left-skewed path pruning structural extremities
    
    # --- Zig-Zag Paths & Complex Negative Traps ---
    ([1, 2, None, None, -3, 4], 4),                           # Path isolates single terminal leaf due to negative blocker
    ([10, 2, 3, 4, 5, -1, -2], 20),                           # Multi-way branches; left subtree wins completely: 4 -> 2 -> 5 -> 10 -> 3 = 24
    ([1, -2, 3, 4, -5, -6, 7], 13)                            # Deep layout: 4 -> -2 -> 1 -> 3 -> 7 = 13? Wait, left side is 4 + (-2) + 1 = 3. Right side is 3 + 7 = 10. Combined = 13. Let's make sure: 4 -> -2 -> 1 -> 3 -> 7 = 13.
])
def test_maxPathSum(input_list, expected):
    """
    Validates max path sum tracking over 15 unique structural variations.
    """
    root = build_tree(input_list)
    assert sol.maxPathSum(root) == expected