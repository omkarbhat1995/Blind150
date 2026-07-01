# Binary Tree Right Side View

Given the root of a binary tree, return the values of the nodes you can see ordered from top to bottom.

## Approach
The most efficient approach is a Breadth-First Search (BFS) using a queue. By traversing the tree level-by-level, we can simply capture the last node of each level to get the "right side view."

- **Time Complexity**: $O(n)$, where $n$ is the number of nodes in the tree, as we visit each node exactly once.
- **Space Complexity**: $O(w)$, where $w$ is the maximum width of the tree (for the queue).

## How to Run Tests
Ensure you have `pytest` installed, then run the following command from the root directory:
```bash
pytest Binary-Tree-Right-Side-View/test_solution.py -v