from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Calculates the diameter of a binary tree.
        The diameter is the longest path between any two nodes.
        """
        self.max_diameter = 0
        
        def dfs(node: Optional[TreeNode]) -> int:
            # Base case: an empty node has a height of 0
            if not node:
                return 0
            
            # Recursively find the height of left and right subtrees
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            
            # The diameter passing THROUGH this specific node is left_height + right_height
            # We update our global maximum if it's the largest we've seen
            self.max_diameter = max(self.max_diameter, left_height + right_height)
            
            # Return the height of the tree rooted at this node to its parent
            return 1 + max(left_height, right_height)
            
        dfs(root)
        return self.max_diameter