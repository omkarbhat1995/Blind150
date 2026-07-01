from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Determines if a binary tree is height-balanced using a bottom-up DFS approach.
        Returns True if balanced, False otherwise.
        """
        def dfs(node: Optional[TreeNode]) -> int:
            # Base case: an empty node has a height of 0
            if not node:
                return 0
            
            # Recursively get the height of the left and right subtrees
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            
            # If either subtree is unbalanced, or if the current node is unbalanced,
            # we return -1 to immediately propagate the failure upward.
            if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
                return -1
                
            # If balanced, return the actual height of the current node
            return 1 + max(left_height, right_height)
            
        # The tree is balanced as long as our DFS doesn't return the -1 error flag
        return dfs(root) != -1