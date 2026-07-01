import pytest
from solution import Solution, TreeNode

def build_tree(values: list) -> TreeNode | None:
    """Helper function to build a binary tree from a LeetCode level-order list."""
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

@pytest.mark.parametrize("input_list, expected_diameter", [
    # Standard Examples
    ([1, None, 2, 3, 4, 5], 3),               # Example 1
    ([1, 2, 3], 2),                           # Example 2
    
    # Minimal Constraints (Smallest Trees)
    ([1], 0),                                 # Single node (0 edges)
    ([1, 2], 1),                              # Root and left child
    ([1, None, 2], 1),                        # Root and right child
    
    # Linear/Skewed Trees (Worst case space complexity)
    ([1, 2, None, 3, None, 4], 3),            # Strictly left-skewed
    ([1, None, 2, None, 3, None, 4], 3),      # Strictly right-skewed
    ([1, 2, None, None, 3, 4], 3),            # Zig-zag skewed
    
    # Perfect & Balanced Trees
    ([1, 2, 3, 4, 5, 6, 7], 4),               # Perfect binary tree depth 3
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 6), # Perfect binary tree depth 4
    
    # Diameter Does NOT Pass Through Root
    # Path: 8-6-4-2-5-7-9 (Length 6), but root is 1
    ([1, 2, 3, 4, 5, None, None, 6, None, None, 7, 8, None, None, 9], 6),
    
    # Imbalanced Trees
    ([1, 2, 3, 4, None, None, 5, 6, None, None, 7], 6), # Deep independent branches
    ([1, 2, 3, 4, 5, None, None, 6, None, 7], 4),       # Left-heavy with internal branching
    
    # Constraint Boundaries & Values
    ([-100, -50, 100, -20, None, 80], 4),     # Negative values (values do not affect diameter)
    ([0] * 15, 6),                            # All identical values (zeros)
])
def test_diameterOfBinaryTree(input_list, expected_diameter):
    """
    Tests the diameterOfBinaryTree method against 15 standard, boundary, and edge cases.
    """
    # 1. Convert standard list to our custom Binary Tree
    root = build_tree(input_list)
    
    # 2. Execute the solution and assert the integer output
    assert sol.diameterOfBinaryTree(root) == expected_diameter