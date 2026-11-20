# Course Schedule II

**Difficulty:** Medium  
**Category:** Graphs / Topological Sort (BFS - Kahn's Algorithm)

## Problem Description
You are given an array `prerequisites` where `prerequisites[i] = [a, b]` indicates that you must take course `b` first if you want to take course `a`.

For example, the pair `[0, 1]` indicates that to take course `0` you have to first take course `1`.

There are a total of `numCourses` courses you are required to take, labeled from `0` to `numCourses - 1`.

Return a valid ordering of courses you can take to finish all courses. If there are many valid answers, return any of them. If it's not possible to finish all courses, return an empty array.
---
## Examples

**Example 1:**
```text
Input: numCourses = 3, prerequisites = [[1,0]]
Output: [0,1,2]
Explanation: We must ensure that course 0 is taken before course 1.
```
**Example 2:**
```text
Input: numCourses = 3, prerequisites = [[0,1],[1,2],[2,0]]
Output: []
Explanation: It's impossible to finish all courses.
```
---
**Constraints**   
* `1 <= numCourses <= 1000`
* `0 <= prerequisites.length <= 1000`
* `All prerequisite pairs are unique.`
---
## Complexity Analysis
* **Time Complexity:** $\mathcal{O}(V + E)$, where $V$ is the number of courses (numCourses) and $E$ is the number of prerequisite pairs (len(prerequisites)). Building the adjacency list and in-degree array takes $\mathcal{O}(V + E)$, and each vertex and edge is processed at most once during the BFS traversal.   
* **Space Complexity:** $\mathcal{O}(V + E)$ to store the adjacency list, the in-degree array, the BFS queue, and the resulting course ordering.
---
## 🧪 Running the Tests

To run the tests for this specific problem, execute the following command in your terminal from the root directory:
```bash
`pytest test_solution.py -v`
```