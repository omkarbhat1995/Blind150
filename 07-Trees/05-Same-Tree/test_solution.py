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

@pytest.mark.parametrize("p_list, q_list, expected", [
    # Basic cases
    ([1, 2, 3], [1, 2, 3], True),
    ([1, 2], [1, None, 2], False),
    ([1, 2, 3], [1, 3, 2], False),
    ([], [], True),
    
    # Structural differences
    ([1], [1, 2], False),
    ([1, 2, None], [1, None, 2], False),
    ([1, 2, 3, 4], [1, 2, 3, 4, 5], False),
    
    # Value differences
    ([1, 2, 3], [1, 2, 4], False),
    ([100], [101], False),
    ([-100, 0], [-100, 1], False),
    
    # Larger trees
    ([1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7], True),
    ([1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 8], False),
    
    # Deep/Skewed trees
    ([1, 2, None, 3, None], [1, 2, None, 3, None], True),
    ([1, 2, None, 3, None], [1, 2, None, 4, None], False),
    
    # Single vs Multi node
    ([1], [], False)
])
def test_isSameTree(p_list, q_list, expected):
    p = build_tree(p_list)
    q = build_tree(q_list)
    assert sol.isSameTree(p, q) == expected