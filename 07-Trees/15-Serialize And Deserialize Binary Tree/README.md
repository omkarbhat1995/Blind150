# Serialize and Deserialize Binary Tree

## Problem Description
Serialization is the process of converting an in-memory data structure into a sequence of bits (or a string) so that it can be stored or transmitted across a network, to be reconstructed later in another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm works, as long as a binary tree can be serialized to a string, and that string can be deserialized back into the original tree structure.

### Constraints
- The number of nodes in the tree is in the range `[0, 1000]`.
- `-1000 <= Node.val <= 1000`

---

## Approach: Pre-Order Traversal (DFS)
While LeetCode natively serializes trees using Level-Order (BFS), doing so requires managing a queue and handling trailing nulls, which can get unnecessarily messy.

Instead, the cleanest and most efficient approach is **Pre-Order DFS (Root $\rightarrow$ Left $\rightarrow$ Right)**:
1. **Serialization:** We traverse the tree in pre-order. We append each node's value to an array. If we hit a `None` (null) node, we append a special marker (like `"N"`). Finally, we join the array into a single comma-separated string.
2. **Deserialization:** We split the comma-separated string back into an array. Using an iterator (or a pointer), we recursively build the tree. Because it was serialized in pre-order, the first element we process is always the root. We then recursively build the left child, and once that completes, we build the right child. Hitting an `"N"` simply returns `None` and halts that branch's recursion.

## Complexity Analysis
- **Time Complexity:** $O(n)$ for both serialization and deserialization, where $n$ is the number of nodes in the tree. We visit and process every node (and its null children) exactly once.
- **Space Complexity:** $O(n)$ for both. The serialized string/array requires space proportional to the number of nodes, and the recursive call stack takes $O(h)$ space, which degrades to $O(n)$ in the worst case (a perfectly skewed tree).