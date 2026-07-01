import pytest
from solution import Solution, TreeNode

def build_tree(values: list) -> TreeNode | None:
    if not values: return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root

sol = Solution()

@pytest.mark.parametrize("root_list, subRoot_list, expected", [
    # Examples
    ([1, 2, 3, 4, 5], [2, 4, 5], True),
    ([1, 2, 3, 4, 5, None, None, 6], [2, 4, 5], False),
    
    # Matches
    ([1, 1], [1], True),
    ([3, 4, 5, 1, 2], [4, 1, 2], True),
    
    # Mismatches (Structure/Values)
    ([3, 4, 5, 1, 2], [4, 1, 3], False),
    ([1, 2, 3], [2, 3], False),
    ([1, 2, 3], [1, 2], False),
    
    # Edge Cases
    ([1], [1], True),
    ([1], [], True), # subRoot empty is technically a subtree
    ([], [1], False),
    ([1, 1], [1, 2], False),
    
    # Skewed/Deep
    ([1, 2, None, 3, None], [2, 3, None], True),
    ([1, 2, None, 3, None], [2, 4, None], False),
    
    # Large/Boundary values
    ([100, -100, 50], [50], True),
    ([1, 2, 2, 3, 3, None, None, 4, 4], [2, 3, 3], False),
])
def test_isSubtree(root_list, subRoot_list, expected):
    root = build_tree(root_list)
    subRoot = build_tree(subRoot_list)
    assert sol.isSubtree(root, subRoot) == expected