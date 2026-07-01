from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        Reconstructs a binary tree from its preorder and inorder traversal arrays.
        Optimized with a hash map lookup for O(n) total time complexity.
        """
        # Map values to their indices in the inorder list for O(1) lookups
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        def array_to_tree(pre_start: int, pre_end: int, in_start: int, in_end: int) -> Optional[TreeNode]:
            if pre_start > pre_end or in_start > in_end:
                return None
            
            # The first element in the preorder range is the root of this subtree
            root_val = preorder[pre_start]
            root = TreeNode(root_val)
            
            # Locate where this root splits the inorder sequence
            root_in_idx = inorder_map[root_val]
            
            # Determine size of the left subtree
            left_subtree_size = root_in_idx - in_start
            
            # Recursively construct the left and right subtrees
            root.left = array_to_tree(
                pre_start + 1, 
                pre_start + left_subtree_size, 
                in_start, 
                root_in_idx - 1
            )
            root.right = array_to_tree(
                pre_start + left_subtree_size + 1, 
                pre_end, 
                root_in_idx + 1, 
                in_end
            )
            
            return root

        return array_to_tree(0, len(preorder) - 1, 0, len(inorder) - 1)