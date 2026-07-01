from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Finds the kth smallest element in a BST using an iterative 
        in-order traversal with early termination.
        """
        stack = []
        curr = root
        
        while curr or stack:
            # Travel to the leftmost node of the current subtree
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # Process the node at the top of our stack
            curr = stack.pop()
            k -= 1
            
            if k == 0:
                return curr.val
            
            # Move to the right subtree
            curr = curr.right
            
        return -1  # Fallback return (guaranteed unreachable per constraints)