# Kth Smallest Element in a BST

## Problem Description
Given the root of a binary search tree (BST) and an integer `k`, return the `k`-th smallest value (1-indexed) of all the values of the nodes in the tree.

A valid BST satisfies the following constraints:
- The left subtree of every node contains only nodes with keys **less than** the node's key.
- The right subtree of every node contains only nodes with keys **greater than** the node's key.
- Both the left and right subtrees are also binary search trees.

### Constraints
- The number of nodes in the tree is `n`.
- `1 <= k <= n <= 1000`
- `0 <= Node.val <= 1000`

---

## Approach: Iterative In-Order Traversal (DFS)
The defining property of a Binary Search Tree is that an **in-order traversal** (Left $\rightarrow$ Root $\rightarrow$ Right) visits the nodes in strictly ascending order. 

Instead of traversing the entire tree, storing all elements in an array, and returning the element at index `k - 1` (which takes $O(n)$ extra space), we can optimize using an **iterative stack-based in-order traversal**:
1. We navigate as far left as possible, pushing all vendor nodes onto a stack.
2. We pop the top node from the stack (which represents the current smallest unvisited value).
3. We decrement `k`. If `k == 0`, we have successfully located our $k$-th smallest element and return its value immediately.
4. We then move to the right child of the popped node and repeat the process.

This **early-termination** mechanism guarantees we only visit exactly `k` nodes.

## Complexity Analysis
- **Time Complexity:** $O(h + k)$ where $h$ is the height of the tree. In the worst case (a highly skewed tree), this takes $O(n)$. In a balanced tree, it takes $O(\log n + k)$.
- **Space Complexity:** $O(h)$ to maintain the explicit call stack, reflecting the depth of the tree branches.