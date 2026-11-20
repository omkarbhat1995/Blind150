# Course Schedule

**Difficulty:** Medium
**Category:** Graphs / Topological Sort (BFS - Kahn's Algorithm)

## Problem Description
You are given an array `prerequisites` where `prerequisites[i] = [a, b]` indicates that you must take course `b` first if you want to take course `a`.

The pair `[0, 1]` indicates that you must take course `1` before taking course `0`.

There are a total of `numCourses` courses you are required to take, labeled from `0` to `numCourses - 1`.

Return `true` if it is possible to finish all courses, otherwise return `false`.
---
## Example
**Example 1:**
```text
Input: numCourses = 2, prerequisites = [[0,1]]
Output: true
Explanation: First take course 1 (no prerequisites) and then take course 0.
```
**Example 2:**
```text
Input: numCourses = 2, prerequisites = [[0,1],[1,0]]
Output: false
Explanation: In order to take course 1 you must take course 0, and to take course 0 you must take course 1. So it is impossible.
```
---
**Constraints:**
* `1 <= numCourses <= 1000`
* `0 <= prerequisites.length <= 1000`
* `prerequisites[i].length == 2`
* `0 <= a[i], b[i] < numCourses`
* `All prerequisite pairs are unique.`
---
## Complexity Analysis
* **Time Complexity:** $\mathcal{O}(V + E)$, where $V$ is the number of courses (numCourses) and $E$ is the number of prerequisite pairs (len(prerequisites)). Building the adjacency list and in-degree array takes $\mathcal{O}(V + E)$, and each vertex and edge is processed at most once during the BFS traversal.
* **Space Complexity:** $\mathcal{O}(V + E)$ to store the adjacency list, the in-degree array, and the BFS queue.
---
## 🧪 Running the Tests

To run the tests for this specific problem, execute the following command in your terminal from the root directory:
```bash
`pytest test_solution.py -v`
```
