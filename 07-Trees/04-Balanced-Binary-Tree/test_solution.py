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

@pytest.mark.parametrize("input_list, expected_balanced", [
    # Standard Examples
    ([1, 2, 3, None, None, 4], True),                   # Example 1
    ([1, 2, 3, None, None, 4, None, 5], False),         # Example 2
    ([], True),                                         # Example 3 (Empty tree)
    
    # Minimal Constraints (Smallest Trees)
    ([1], True),                                        # Single node
    ([1, 2], True),                                     # Root and left child (Diff = 1)
    ([1, None, 2], True),                               # Root and right child (Diff = 1)
    
    # Skewed Trees (Unbalanced lines)
    ([1, 2, None, 3], False),                           # Left-skewed (Diff = 2)
    ([1, None, 2, None, 3], False),                     # Right-skewed (Diff = 2)
    ([1, 2, None, None, 3, 4], False),                  # Zig-zag skewed
    
    # Perfect & Complete Trees (Fully Balanced)
    ([1, 2, 3], True),                                  # Small balanced triangle
    ([1, 2, 3, 4, 5, 6, 7], True),                      # Perfect binary tree depth 3
    ([1, 2, 3, 4, 5], True),                            # Complete binary tree depth 3
    
    # Structurally Tricky Imbalances
    ([1, 2, 2, 3, 3, None, None, 4, 4], False),         # Famous LeetCode trap (Root looks balanced, but left branch is unbalanced internally)
    ([1, 2, 3, 4, None, None, 5, 6, None, None, 7], False), # Deep independent branches differing by 2
    
    # Constraint Boundaries & Values
    ([-1000, 1000, -500], True),                        # Negative bounds check (Values don't affect structure)
    ([0, 0, 0, 0, 0, 0, None, 0], True),                # All identical values, balanced configuration
])
def test_isBalanced(input_list, expected_balanced):
    """
    Tests the isBalanced method against 15+ standard, boundary, and edge cases.
    """
    # 1. Convert standard list to our custom Binary Tree
    root = build_tree(input_list)
    
    # 2. Execute the solution and assert the boolean output
    assert sol.isBalanced(root) == expected_balanced