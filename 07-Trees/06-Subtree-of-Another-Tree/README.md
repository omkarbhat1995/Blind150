# Subtree of Another Tree

**Difficulty:** Easy
**Topics:** Trees, Depth-First Search (DFS), Binary Tree

## Problem Description

Given the roots of two binary trees `root` and `subRoot`, return `true` if there is a subtree of `root` with the same structure and node values of `subRoot` and `false` otherwise.

A subtree of a binary tree `tree` is a tree that consists of a node in `tree` and all of this node's descendants. The tree `tree` could also be considered as a subtree of itself.

**Example 1:**
* **Input:** `root = [1,2,3,4,5]`, `subRoot = [2,4,5]`
* **Output:** `true`

**Example 2:**
* **Input:** `root = [1,2,3,4,5,null,null,6]`, `subRoot = [2,4,5]`
* **Output:** `false`

## Approach

This problem can be broken down into two recursive functions:
1.  **`isSameTree(p, q)`**: A helper function to check if two trees are identical in structure and value. This is the exact same logic we used for the "Same Binary Tree" problem.
2.  **`isSubtree(root, subRoot)`**:
    * If `subRoot` is null, it is technically a subtree of any tree (return `True`).
    * If `root` is null, it cannot contain a non-null subtree (return `False`).
    * If `isSameTree(root, subRoot)` is true, we found a match (return `True`).
    * Otherwise, recurse down to both `root.left` and `root.right` to see if the match exists deeper in the tree.

## Complexity Analysis
* **Time Complexity:** $O(m \times n)$ where $n$ is the number of nodes in the main tree and $m$ is the number of nodes in the `subRoot` tree. In the worst case, for every node in `root`, we perform an $O(m)$ comparison.
* **Space Complexity:** $O(h)$ where $h$ is the height of the tree, representing the recursion stack depth.