# Invert Binary Tree

**Difficulty:** Easy
**Topics:** Tree, Depth-First Search, Breadth-First Search, Binary Tree

## Problem Description

You are given the `root` of a binary tree. Invert the binary tree and return its `root`.

## Approach: Recursive Depth-First Search (DFS)

The most elegant way to solve this problem is using recursion. An inverted binary tree means that for every node, its left and right children are swapped.

1. **Base Case:** If the current `root` is `None`, we simply return `None`. This handles empty trees and prevents us from operating on non-existent leaf children.
2. **Recursive Step:** We recursively call our invert function on the left child and the right child.
3. **Swap:** Once the recursive calls return the inverted subtrees, we swap the current node's `left` and `right` pointers.
4. **Return:** Finally, we return the current `root`.

## Complexity
- **Time Complexity:** $O(n)$ where `n` is the number of nodes in the tree. We visit every single node exactly once.
- **Space Complexity:** $O(h)$ where `h` is the height of the tree. This accounts for the recursive call stack. In the worst-case scenario (a completely skewed tree), this degrades to $O(n)$. In the best-case (a completely balanced tree), it is $O(\log n)$.