# Binary Tree Level Order Traversal

**Difficulty:** Medium
**Topics:** Trees, Breadth-First Search (BFS), Binary Tree

## Problem Description

Given the `root` of a binary tree, return the level order traversal of its nodes' values as a nested list (i.e., from left to right, level by level).

**Example 1:**
* **Input:** `root = [1,2,3,4,5,6,7]`
* **Output:** `[[1],[2,3],[4,5,6,7]]`

**Constraints:**
* The number of nodes in the tree is in the range `[0, 1000]`.
* `-1000 <= Node.val <= 1000`

## Approach

The most efficient way to solve this is using a **Breadth-First Search (BFS)** with a **Queue**:
1. Use a queue to keep track of nodes to visit, starting with the `root`.
2. While the queue is not empty, get the current size of the queue (this represents the number of nodes at the current level).
3. Iterate through that specific number of nodes, processing them one by one.
4. For each node, append its value to a `current_level` list, and add its children (if they exist) to the queue for the next level.
5. Once all nodes at the current level are processed, add `current_level` to your `result` list.

## Complexity Analysis
* **Time Complexity:** $O(n)$ where $n$ is the number of nodes in the tree. We visit each node exactly once.
* **Space Complexity:** $O(w)$ where $w$ is the maximum width of the tree. In the worst case (a perfect binary tree), the width at the bottom level can be approximately $n/2$, resulting in $O(n)$ space for the queue.