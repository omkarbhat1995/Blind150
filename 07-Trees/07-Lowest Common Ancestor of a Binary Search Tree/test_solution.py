import pytest
from solution import Solution, TreeNode

# Helper to build BST from sorted list (to ensure valid BST structure)
def build_bst(values: list) -> TreeNode | None:
    if not values: return None
    mid = len(values) // 2
    root = TreeNode(values[mid])
    root.left = build_bst(values[:mid])
    root.right = build_bst(values[mid+1:])
    return root

# Helper to find a node by value (needed for tests)
def find_node(root, val):
    if not root: return None
    if root.val == val: return root
    return find_node(root.left, val) if val < root.val else find_node(root.right, val)

sol = Solution()

@pytest.mark.parametrize("nodes, p_val, q_val, expected_lca", [
    # Standard Examples
    ([1, 2, 3, 4, 5, 7, 8, 9], 3, 8, 5),          # LCA is root (5)
    ([1, 2, 3, 4, 5, 7, 8, 9], 3, 4, 3),          # LCA is p (3)
    
    # Relationships
    ([1, 2, 3, 4, 5, 7, 8, 9], 2, 4, 3),          # LCA is parent of p and q
    ([1, 2, 3, 4, 5, 7, 8, 9], 7, 9, 8),          # LCA is right child of root
    
    # Boundary Conditions
    ([1, 2, 3, 4, 5, 7, 8, 9], 1, 9, 5),          # LCA is root (far left, far right)
    ([1, 2, 3, 4, 5, 7, 8, 9], 1, 2, 2),          # LCA is parent of p
    
    # Skewed Tree (Linear structure)
    ([1, 2, 3, 4, 5], 1, 3, 3),                   # Linear left-heavy
    ([1, 2, 3, 4, 5], 3, 5, 3),                   # Linear right-heavy
    
    # Single Branch Checks
    ([1, 2, 3, 4, 5], 2, 5, 3),                   # p is ancestor of q
    ([1, 2, 3, 4, 5], 5, 2, 3),                   # q is ancestor of p (order swapped)
    
    # Negative Values
    ([-100, -50, 0, 50, 100], -100, 0, 00),
    ([-100, -50, 0, 50, 100], -100, 100, 0),
    
    # Small Trees
    ([1, 2], 1, 2, 2),
    ([1, 2, 3], 1, 3, 2),
    ([1, 2, 3], 1, 2, 2)
])
def test_lowestCommonAncestor(nodes, p_val, q_val, expected_lca):
    root = build_bst(nodes)
    p = find_node(root, p_val)
    q = find_node(root, q_val)
    root = build_bst(nodes)
    print(f"\nTesting with tree structure:")
    print_tree(root)
    assert sol.lowestCommonAncestor(root, p, q).val == expected_lca 

def print_tree(node, level=0):
    if node:
        print_tree(node.right, level + 1)
        print(' ' * 4 * level + '-> ' + str(node.val))
        print_tree(node.left, level + 1)

