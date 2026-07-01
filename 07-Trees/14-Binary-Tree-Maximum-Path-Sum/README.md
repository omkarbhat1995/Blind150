# Binary Tree Maximum Path Sum

## Problem Description
Given the root of a non-empty binary tree, return the maximum path sum of any non-empty path.

A path in a binary tree is defined as a sequence of nodes where each pair of adjacent nodes has an edge connecting them. A node can not appear in the sequence more than once. The path does not necessarily need to include the root node.

The path sum is calculated as the sum of the node values within that path sequence.

### Constraints
- The number of nodes in the tree is in the range `[1, 1000]`.
- `-1000 <= Node.val <= 1000`

---

## Approach: Post-Order DFS with Global Maximum Tracking
Because a path can start and end at any node in the tree, we look at this problem from the perspective of each individual node acting as the "highest point" (or bridge) of a potential path.

1. We use a recursive depth-first search helper function that returns the **maximum single-path contribution** a subtree can offer to its parent node.
2. For any given node, its single-path contribution can only include either its left child branch or its right child branch, plus itself. If a branch returns a negative sum, we choose to ignore it completely (clamp it to `0`).
3. Simultaneously, at each node, we compute the value of the path that "splits" or hooks through this node: `node.val + left_gain + right_gain`.
4. We compare this combined path sum against a global maximum tracking variable (`max_sum`) and update it accordingly.

This allows us to check all paths that bridge across distinct subtrees without recalculating nodes multiple times.

## Complexity Analysis
- **Time Complexity:** $O(n)$ where $n$ is the number of nodes in the tree. We visit each individual node exactly once.
- **Space Complexity:** $O(h)$ where $h$ is the height of the tree, representing the allocation on the recursive call stack. In the worst-case scenario (a skewed tree), this degrades to $O(n)$.