from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Validates if a binary tree is a proper Binary Search Tree.
        Uses DFS tracking valid lower and upper boundaries dynamically.
        """
        def validate(node: Optional[TreeNode], low: float, high: float) -> bool:
            # An empty tree/leaf child is technically a valid BST
            if not node:
                return True
            
            # Current node value must strictly respect the current boundary constraints
            if not (low < node.val < high):
                return False
            
            # Left subtree elements must be < node.val
            # Right subtree elements must be > node.val
            return validate(node.left, low, node.val) and validate(node.right, node.val, high)

        return validate(root, float('-inf'), float('+inf'))