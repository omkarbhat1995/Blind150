import pytest
from collections import deque
from solution import Solution, TreeNode
from typing import List, Optional

def build_tree(nodes: List[Optional[int]]) -> Optional[TreeNode]:
    if not nodes: return None
    root = TreeNode(nodes[0])
    queue = deque([root])
    i = 1
    while queue and i < len(nodes):
        node = queue.popleft()
        if i < len(nodes) and nodes[i] is not None:
            node.left = TreeNode(nodes[i])
            queue.append(node.left)
        i += 1
        if i < len(nodes) and nodes[i] is not None:
            node.right = TreeNode(nodes[i])
            queue.append(node.right)
        i += 1
    return root

sol = Solution()

@pytest.mark.parametrize("input_list, expected", [
    # Examples
    ([3,1,4,3,None,1,5], 4),
    ([3,3,None,4,2], 3),
    ([1], 1),
    # Edge Cases
    ([], 0),
    ([2,1,1,3,None,1,5], 3), # Example 1
    ([1,2,-1,3,4], 4),       # Example 2
    ([-1, -5, -2, -6, -3], 1), # Negative values
    ([10, 10, 10, 10], 4),    # All identical
    ([1, 2, 3, 4, 5, 6, 7], 7), # Strictly increasing
    ([7, 6, 5, 4, 3, 2, 1], 1), # Strictly decreasing
    ([1, None, 2, None, 3, None, 4], 4), # Right skew
    ([4, 3, None, 2, None, 1], 1),
    ([5, 5, 5, 5, 5, 5], 6),
    ([1, 0, 1, 0, 1], 3),
    ([2, 4, 4, 3, None, None, None], 3)
])
def test_goodNodes(input_list, expected):
    root = build_tree(input_list)
    assert sol.goodNodes(root) == expected