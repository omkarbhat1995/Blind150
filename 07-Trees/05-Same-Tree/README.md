# Same Binary Tree

**Difficulty:** Easy
**Topics:** Trees, Depth-First Search (DFS), Binary Tree

## Problem Description

Given the roots of two binary trees `p` and `q`, return `true` if the trees are equivalent, otherwise return `false`.

Two binary trees are considered equivalent if they share the exact same structure and the nodes have the same values.

## Approach

The most efficient way to solve this is using a **Recursive Depth-First Search (DFS)**. We can compare the two trees simultaneously:
1. **Base Case 1:** If both nodes are `None`, they are identical, return `True`.
2. **Base Case 2:** If one node is `None` but the other is not, the structures differ, return `False`.
3. **Comparison:** If the values of the current nodes differ, return `False`.
4. **Recursion:** Return `True` if both the left subtrees are the same **AND** the right subtrees are the same.

## Complexity Analysis
* **Time Complexity:** $O(n)$ where $n$ is the number of nodes in the trees. We visit every node to ensure equality.
* **Space Complexity:** $O(h)$ where $h$ is the height of the tree, representing the recursion stack depth.