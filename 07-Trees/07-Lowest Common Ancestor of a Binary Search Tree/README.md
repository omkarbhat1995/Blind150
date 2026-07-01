# Lowest Common Ancestor in Binary Search Tree

**Difficulty:** Medium
**Topics:** Trees, Binary Search Tree (BST), Depth-First Search (DFS)

## Problem Description

Given a binary search tree (BST) where all node values are unique, and two nodes from the tree `p` and `q`, return the lowest common ancestor (LCA) of the two nodes.

The LCA between two nodes `p` and `q` is the lowest node in a tree `T` such that both `p` and `q` are descendants (where a node is allowed to be a descendant of itself).

## Approach

Because this is a **BST**, we have a powerful property: for any node, all nodes in the left subtree are smaller, and all nodes in the right subtree are larger.

We can exploit this to find the LCA:
1. Start at the root.
2. If both `p` and `q` are smaller than the current node, the LCA must be in the left subtree.
3. If both `p` and `q` are larger than the current node, the LCA must be in the right subtree.
4. If one is smaller and one is larger (or if the current node is either `p` or `q`), we have found the split point—this is the LCA.

## Complexity Analysis
* **Time Complexity:** **O(h)** where `h` is the height of the tree. In the worst case (a skewed tree), it is $O(n)$, but for a balanced tree, it is $O(\log n)$.
* **Space Complexity:** **O(h)** due to the recursion stack. You can also implement this iteratively to achieve **O(1)** space.