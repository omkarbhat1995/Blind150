import pytest
from typing import List, Optional
from solution import TreeNode, Codec

def build_tree(nodes: List[Optional[int]]) -> Optional[TreeNode]:
    """Helper to build a tree from LeetCode's level-order array format."""
    if not nodes:
        return None
    
    root = TreeNode(nodes[0])
    queue = [root]
    i = 1
    
    while queue and i < len(nodes):
        current = queue.pop(0)
        
        if nodes[i] is not None:
            current.left = TreeNode(nodes[i])
            queue.append(current.left)
        i += 1
        
        if i < len(nodes) and nodes[i] is not None:
            current.right = TreeNode(nodes[i])
            queue.append(current.right)
        i += 1
        
    return root

def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    """Helper to verify structural and value equality between two trees."""
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

@pytest.mark.parametrize("input_list", [
    # --- Standard LeetCode Examples ---
    ([1, 2, 3, None, None, 4, 5]),              # Example 1
    ([]),                                       # Example 2 (Empty Tree)
    
    # --- Single Element & Small Trees ---
    ([1]),                                      # Single root node
    ([1, 2]),                                   # Only left child
    ([1, None, 2]),                             # Only right child
    
    # --- Constraint Boundaries ---
    ([-1000, 1000, -500, 500]),                 # Min and Max value constraints
    ([0, 0, 0, 0, 0]),                          # All zeros
    ([5, 5, 5, 5, 5]),                          # All identical values
    
    # --- Skewed Trees ---
    ([1, 2, None, 3, None, 4]),                 # Strictly left-skewed
    ([1, None, 2, None, 3, None, 4]),           # Strictly right-skewed
    ([1, 2, None, None, 3, 4]),                 # Zig-zag structure
    
    # --- Balanced & Complex Structures ---
    ([1, 2, 3, 4, 5, 6, 7]),                    # Perfectly balanced (Full Binary Tree)
    ([-1, -2, -3, -4, -5, -6, -7]),             # All negative values
    ([100, 50, 200, 25, 75, 150, 300]),         # Standard BST layout
    ([1, None, 2, 3, None, 4, 5, None, None, 6])# Deep asymmetrical tree
])
def test_codec(input_list):
    """
    Validates that a tree can be serialized and deserialized back into its exact original structure.
    """
    # 1. Build original tree
    original_root = build_tree(input_list)
    
    # 2. Initialize codec
    ser = Codec()
    deser = Codec()
    
    # 3. Serialize to string
    serialized_string = ser.serialize(original_root)
    
    # 4. Deserialize back to tree
    reconstructed_root = deser.deserialize(serialized_string)
    
    # 5. Assert structural equality
    assert is_same_tree(original_root, reconstructed_root) is True