# Balanced Binary Tree

**Difficulty:** Easy
**Topics:** Trees, Depth-First Search (DFS), Binary Tree

## Problem Description

Given a binary tree, return `true` if it is height-balanced and `false` otherwise.

A height-balanced binary tree is defined as a binary tree in which the left and right subtrees of *every* node differ in height by no more than 1.

**Example 1:**
* **Input:** `root = [1,2,3,null,null,4]`
* **Output:** `true`

**Example 2:**
* **Input:** `root = [1,2,3,null,null,4,null,5]`
* **Output:** `false`

**Example 3:**
* **Input:** `root = []`
* **Output:** `true`

**Constraints:**
* The number of nodes in the tree is in the range `[0, 1000]`.
* `-1000 <= Node.val <= 1000`

## Approach

The most optimal way to solve this is using a **Bottom-Up Depth-First Search (DFS)**. 
Instead of calculating the height of the left and right subtrees independently for every single node (which results in an inefficient $O(n^2)$ time complexity), we can calculate the height and check the balance simultaneously.

As our DFS reaches the leaf nodes and bubbles back up, we check the height difference. If any subtree is ever found to be unbalanced (difference $> 1$), we immediately return `-1` to flag it. If a parent node receives a `-1` from either child, it knows the tree is unbalanced and passes the `-1` further up the chain, short-circuiting unnecessary calculations.

## Complexity Analysis
* **Time Complexity:** **O(n)** where `n` is the number of nodes in the tree. We visit every single node exactly once.
* **Space Complexity:** **O(h)** where `h` is the height of the tree. This accounts for the memory used by the recursion stack. In the worst-case scenario (a skewed tree), the space complexity becomes **O(n)**. For a balanced tree, it operates in **O(log n)** space.