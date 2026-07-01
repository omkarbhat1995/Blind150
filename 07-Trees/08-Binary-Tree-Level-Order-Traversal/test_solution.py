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

@pytest.mark.parametrize("input_list, expected_output", [
    # Standard Examples
    ([1, 2, 3, 4, 5, 6, 7], [[1], [2, 3], [4, 5, 6, 7]]),
    ([1], [[1]]),
    ([], []),
    
    # Skewed Trees
    ([1, 2, None, 3, None, 4], [[1], [2], [3], [4]]),   # Left-skewed
    ([1, None, 2, None, 3, None, 4], [[1], [2], [3], [4]]), # Right-skewed
    
    # Partial Trees
    ([1, 2, 3, 4, None, None, 5], [[1], [2, 3], [4, 5]]),
    ([1, 2, 3, None, 4, 5, None], [[1], [2, 3], [4, 5]]),
    
    # Boundary Values
    ([1000, -1000, 0], [[1000], [-1000, 0]]),
    ([0, 0, 0, 0, 0], [[0], [0, 0], [0, 0]]),
    
    # Various Depths
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [[1], [2, 3], [4, 5, 6, 7], [8, 9, 10, 11]]),
    ([1, 2, 3, None, 4, 5, None, None, 6], [[1], [2, 3], [4, 5], [6]]),
    ([1, 2], [[1], [2]]),
    ([1, None, 2], [[1], [2]]),
    ([1, 2, 3, 4], [[1], [2, 3], [4]]),
    ([1, 2, 3, None, None, 4, 5], [[1], [2, 3], [4, 5]])
])
def test_levelOrder(input_list, expected_output):
    root = build_tree(input_list)
    assert sol.levelOrder(root) == expected_output