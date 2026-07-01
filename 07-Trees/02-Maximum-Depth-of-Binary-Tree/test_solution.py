import pytest
from solution import Solution, TreeNode

def build_tree(values: list) -> TreeNode | None:
    """Helper function to build a binary tree from a level-order list."""
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    
    while queue and i < len(values):
        node = queue.pop(0)
        
        # Assign left child
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        # Assign right child
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
        
    return root

# Initialize the solution object
sol = Solution()

@pytest.mark.parametrize("input_list, expected_depth", [
    # Standard Examples
    ([1, 2, 3, None, None, 4], 3),            # Example 1 mapping
    ([], 0),                                  # Example 2 (Empty tree)
    
    # Single Node & Minimal Trees
    ([1], 1),                                 # Only root
    ([1, 2], 2),                              # Root and left child
    ([1, None, 2], 2),                        # Root and right child
    ([1, 2, 3], 2),                           # Balanced 3-node tree
    
    # Skewed Trees (Worst Case Space Complexity)
    ([1, 2, None, 3, None, 4, None], 4),      # Strictly left-skewed
    ([1, None, 2, None, 3, None, 4], 4),      # Strictly right-skewed
    ([1, 2, None, None, 3, 4, None], 4),      # Zig-zag structure
    
    # Perfectly Balanced Trees
    ([1, 2, 3, 4, 5, 6, 7], 3),               # Perfect binary tree depth 3
    ([1] * 31, 5),                            # Perfect binary tree depth 5 (31 nodes)
    
    # Imbalanced & Complex Trees
    ([1, 2, 3, None, None, 4, 5], 3),         # Right heavy leaves
    ([1, 2, 3, 4, None, None, 5, 6, None, None, 7], 4), # Complex deep branching
    
    # Constraint Boundaries & Values
    ([-100, -50, 100, -20, None, 80], 3),     # Negative values (bounds check)
    ([0, 0, 0, 0, None, None, 0], 3),         # All identical values (zeros)
])
def test_maxDepth(input_list, expected_depth):
    """
    Tests the maxDepth method against 15 standard, boundary, and edge cases.
    """
    # 1. Convert standard list to our custom Binary Tree
    root = build_tree(input_list)
    
    # 2. Execute the solution and assert the integer output
    assert sol.maxDepth(root) == expected_depth