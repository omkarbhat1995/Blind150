# Maximum Depth of Binary Tree

**Difficulty:** Easy
**Topics:** Trees, Depth-First Search (DFS), Breadth-First Search (BFS), Binary Tree

## Problem Description

Given the `root` of a binary tree, return its depth.

The depth of a binary tree is defined as the number of nodes along the longest path from the root node down to the farthest leaf node.

**Example 1:**
* **Input:** `root = [1,2,3,null,null,4]`
* **Output:** `3`

**Example 2:**
* **Input:** `root = []`
* **Output:** `0`

**Constraints:**
* `0 <= The number of nodes in the tree <= 100`
* `-100 <= Node.val <= 100`

## Approach

The most elegant way to solve this is using a **Recursive Depth-First Search (DFS)**. 
We can determine the maximum depth of the tree by asking: *"What is the maximum depth of my left subtree, and what is the maximum depth of my right subtree?"* Once we have those two values, the depth of the current node is simply the maximum of those two sub-depths, plus `1` (to account for the current node itself). The base case for our recursion is when we hit an empty node (`None`), which contributes a depth of `0`.

## Complexity Analysis
* **Time Complexity:** **O(n)** where `n` is the number of nodes in the tree. We must visit every single node exactly once to determine the max depth.
* **Space Complexity:** **O(h)** where `h` is the height of the tree. This accounts for the memory used by the recursion stack. In the worst-case scenario (a completely skewed tree), the space complexity becomes **O(n)**. For a perfectly balanced tree, it operates in **O(log n)** space.