from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Determines if two binary trees are identical in structure and value.
        """
        # Both are empty
        if not p and not q:
            return True
        
        # One is empty, one is not, or values differ
        if not p or not q or p.val != q.val:
            return False
        
        # Recursively check subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)