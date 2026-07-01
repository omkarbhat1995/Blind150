# Diameter of Binary Tree

**Difficulty:** Easy
**Topics:** Trees, Depth-First Search (DFS), Binary Tree

## Problem Description

The **diameter** of a binary tree is defined as the length of the longest path between any two nodes within the tree. The path does not necessarily have to pass through the root.

The length of a path between two nodes in a binary tree is the number of edges between the nodes. Note that the path can not include the same node twice.

Given the `root` of a binary tree, return the diameter of the tree.

**Example 1:**
* **Input:** `root = [1,null,2,3,4,5]`
* **Output:** `3`
* **Explanation:** `3` is the length of the path `[1,2,3,5]` or `[5,3,2,4]`.

**Example 2:**
* **Input:** `root = [1,2,3]`
* **Output:** `2`

**Constraints:**
* `1 <= number of nodes in the tree <= 100`
* `-100 <= Node.val <= 100`

## Approach

We can solve this problem using a bottom-up **Depth-First Search (DFS)**. 
The diameter of a tree at any given node is simply the maximum depth of its left subtree plus the maximum depth of its right subtree. However, the longest path in the entire tree might not pass through the global root node! 

To handle this, we maintain a variable (often a class attribute or an array passed by reference) to track the `max_diameter` seen so far. As our DFS recursively calculates the height of each node to return to its parent, it simultaneously updates `max_diameter` if the sum of the left and right heights at the current node is greater than the running maximum.

## Complexity Analysis
* **Time Complexity:** $O(n)$ where `n` is the number of nodes in the tree. We visit every single node exactly once.
* **Space Complexity:** $O(h)$ where `h` is the height of the tree, representing the memory used by the recursion stack. In the worst-case scenario (a completely skewed tree), this becomes $O(n)$.