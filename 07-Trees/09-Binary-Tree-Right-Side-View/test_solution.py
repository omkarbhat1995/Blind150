import pytest
from solution import Solution, TreeNode
from typing import List, Optional
from collections import deque

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
    # Standard Examples
    ([1,2,3,None,5,None,4], [1,3,4]),
    ([1,None,3], [1,3]),
    ([], []),
    # Edge Cases
    ([1], [1]),
    ([1,2], [1,2]),
    ([1,None,2,None,3], [1,2,3]), # Skewed right
    ([1,2,None,3,None], [1,2,3]), # Skewed left
    ([1,2,3,4,5,6,7], [1,3,7]),   # Full tree
    # Complex Cases
    ([1,2,3,4,None,None,None,5], [1,3,4,5]),
    ([1,2,3,4,5,6,7,8], [1,3,7,8]),
    ([1,2,3,None,5,6,None], [1,3,6]),
    ([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], [1,3,7,15]),
    # Negative Values
    ([-1, -2, -3, None, -5], [-1, -3, -5]),
    ([0, 0, 0, 0], [0, 0, 0]),
    ([1, 2, None, 4, None, 6], [1, 2, 4, 6])
])
def test_rightSideView(input_list, expected):
    root = build_tree(input_list)
    assert sol.rightSideView(root) == expected