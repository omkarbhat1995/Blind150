from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        Calculates the maximum path sum of any non-empty path in a binary tree.
        Tracks a global maximum while returning the max straight path contribution.
        """
        # Initialize global maximum to negative infinity
        self.max_sum = float('-inf')
        
        def gain_from_subtree(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            # Recursively compute the maximum single-path gain from left and right subtrees.
            # If the gain is negative, ignore that branch completely by clamping to 0.
            left_gain = max(gain_from_subtree(node.left), 0)
            right_gain = max(gain_from_subtree(node.right), 0)
            
            # Price of connecting the current node as a bridge joining both subtrees
            current_path_sum = node.val + left_gain + right_gain
            
            # Update the global maximum if this combined path is superior
            self.max_sum = max(self.max_sum, current_path_sum)
            
            # For the parent call stack, return the maximum single branch contribution
            return node.val + max(left_gain, right_gain)

        gain_from_subtree(root)
        return int(self.max_sum)