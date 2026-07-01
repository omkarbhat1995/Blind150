# Construct Binary Tree from Preorder and Inorder Traversal

## Problem Description
Given two integer arrays `preorder` and `inorder` where `preorder` is the preorder traversal of a binary tree and `inorder` is the inorder traversal of the same tree, reconstruct and return the binary tree.

### Properties of Traversal Orders:
- **Preorder:** Visits nodes in the order (Root $\rightarrow$ Left $\rightarrow$ Right). The first element is always the root of the current subtree.
- **Inorder:** Visits nodes in the order (Left $\rightarrow$ Root $\rightarrow$ Right). Elements to the left of the root value belong to the left subtree, and elements to the right belong to the right subtree.

### Constraints
- `1 <= inorder.length <= 1000`
- `inorder.length == preorder.length`
- `-1000 <= preorder[i], inorder[i] <= 1000`
- Both `preorder` and `inorder` consist of **unique** values.

---

## Approach: Recursive Divide and Conquer (Hash Map Optimized)
1. **Identify the Root:** The first element of the current `preorder` segment is always the root node.
2. **Find the Partition:** Locate this root value within the `inorder` array. Everything to its left forms the left subtree, and everything to its right forms the right subtree.
3. **Optimize Lookups:** Scanning `inorder` for the root index takes $O(n)$ time per step, resulting in an $O(n^2)$ overall runtime. We optimize this down to $O(1)$ lookup time by precomputing a hash map mapping each value to its index in the `inorder` array.
4. **Recurse:** Count the number of nodes in the left subtree to precisely slice the corresponding segments out of the `preorder` array, then recursively repeat the process for both children.

## Complexity Analysis
- **Time Complexity:** $O(n)$ where $n$ is the number of nodes. We process each element exactly once, and hash map lookups take $O(1)$ time.
- **Space Complexity:** $O(n)$ to store the index lookup hash map, plus an additional $O(h)$ (where $h$ is the tree height) for the recursive call stack.