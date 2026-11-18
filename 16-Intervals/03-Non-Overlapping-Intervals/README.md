# Non-overlapping Intervals

**Difficulty:** Medium
**Category:** Intervals / Greedy

## Problem Description
Given an array of intervals `intervals` where `intervals[i] = [start_i, end_i]`, return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

*Note: Intervals are non-overlapping even if they have a common point. For example, [1, 3] and [2, 4] are overlapping, but [1, 2] and [2, 3] are non-overlapping.*
---
**Example 1:**
```text
Input: intervals = [[1,2],[2,4],[1,4]]
Output: 1
Explanation: After [1,4] is removed, the rest of the intervals are non-overlapping.
```
**Example 2:**
```text
Input: intervals = [[1,2],[2,4]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
```
---
**Constraints:**
* `1 <= intervals.length <= 100,000`
* `intervals[i].length == 2-5000`
* `0 <= start_i < end_i <= 50000`
---
## Complexity Analysis
* **Time Complexity:** $\mathcal{O}(N \log N)$ where $N$ is the number of intervals. Sorting the array dominates the time complexity, followed by a single $\mathcal{O}(N)$ linear pass.
* **Space Complexity:** $\mathcal{O}(1)$ or $\mathcal{O}(N)$ depending on the language's native sorting algorithm implementation (Python's Timsort uses $\mathcal{O}(N)$ space in the worst case).
---
## 🧪 Running the Tests

To run the tests for this specific problem, execute the following command in your terminal from the root directory:
```bash
`pytest test_solution.py -v`
```