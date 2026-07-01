# Validate Binary Search Tree

## Problem Description
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:
- The left subtree of a node contains only nodes with keys **less than** the node's key.
- The right subtree of a node contains only nodes with keys **greater than** the node's key.
- Both the left and right subtrees must also be binary search trees.

### Constraints
- The number of nodes in the tree is in the range `[1, 1000]`.
- `-1000 <= Node.val <= 1000`

---

## Approach: Recursive Traversal with Bounds (DFS)
A common trap is only checking if a node's value is greater than its left child and less than its right child. However, *all* nodes in the left subtree must be less than the root, and *all* nodes in the right subtree must be greater.

To solve this optimally in a single pass:
1. We pass down a sliding range of valid values defined by a `low` and `high` boundary.
2. Initially, the root can be any value, so `low = -infinity` and `high = infinity`.
3. When we move to the **left child**, the upper bound updates: the child's value must be strictly less than the current node's value (`high = node.val`).
4. When we move to the **right child**, the lower bound updates: the child's value must be strictly greater than the current node's value (`low = node.val`).
5. If any node violates its bounds, we return `False`.

## Complexity Analysis
- **Time Complexity:** $O(n)$ where $n$ is the number of nodes in the tree, as we visit each node exactly once.
- **Space Complexity:** $O(h)$ where $h$ is the height of the tree, representing the memory consumed by the recursive call stack. In the worst case (a completely skewed tree), this takes $O(n)$ space.