# Clone Graph

**Difficulty:** Medium
**Category:** Graphs (BFS / DFS / Hash Map)

## Problem Description
Given a node in a connected undirected graph, return a deep copy of the graph.

Each node in the graph contains an integer value and a list of its neighbors
---
**Example 1:**
```text
Input: adjList = [[2],[1,3],[2]]
Output: [[2],[1,3],[2]]
Explanation: There are 3 nodes in the graph.
Node 1: val = 1 and neighbors = [2].
Node 2: val = 2 and neighbors = [1, 3].
Node 3: val = 3 and neighbors = [2].
```
**Example 2:**
```text
Input: adjList = [[]]
Output: [[]]
Explanation: The graph has one node with no neighbors.
```
**Example 3:**
```text
Input: adjList = []
Output: []
Explanation: The graph is empty.
```
---
**Constraints:**
* `0 <= The number of nodes in the graph <= 100`
* `1 <= Node.val <= 100`
* There are no duplicate edges and no self-loops in the graph.
---
## Complexity Analysis
* **Time Complexity:** $\mathcal{O}(V + E)$ where $V$ is the number of nodes (vertices) and $E$ is the number of edges. Each node and edge is traversed once during the BFS.
* **Space Complexity:** $\mathcal{O}(V)$ for the hash map storing original-to-clone node references and the BFS queue.
---
## 🧪 Running the Tests

To run the tests for this specific problem, execute the following command in your terminal from the root directory:
```bash
`pytest test_solution.py -v`
```