# Count Good Nodes in Binary Tree

Given the root of a binary tree, return the number of "good" nodes. A node is considered good if the path from the root to that node contains no nodes with a value greater than the node's value.

## Approach
We use a recursive DFS traversal. By passing the `max_so_far` value down the recursion stack, we can compare each node's value to the maximum value encountered on its path from the root in $O(1)$ time.

- **Time Complexity**: $O(n)$, where $n$ is the number of nodes in the tree, as we visit each node exactly once.
- **Space Complexity**: $O(h)$, where $h$ is the height of the tree (recursion stack).

## How to Run Tests
```bash
pytest Count-Good-Nodes-in-Binary-Tree/test_solution.py -v