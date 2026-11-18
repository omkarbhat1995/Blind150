# Merge Intervals

**Difficulty:** Medium
**Category:** Arrays / Intervals / Sorting

## Problem Description
Given an array of intervals where `intervals[i] = [start_i, end_i]`, merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

You may return the answer in any order.

*Note: Intervals are non-overlapping if they have no common point. For example, `[1, 2]` and `[3, 4]` are non-overlapping, but `[1, 2]` and `[2, 3]` are overlapping.*
---
**Example 1:**
```text
Input: intervals = [[1,3],[1,5],[6,7]]
Output: [[1,5],[6,7]]
Explanation: [1,3] and [1,5] overlap, so they are merged into [1,5].
```
**Example 2:**
```text
Input: intervals = [[1,2],[2,3]]
Output: [[1,3]]
Explanation: Intervals [1,2] and [2,3] have a common point and are considered overlapping.
```
---
**Constraints:**
* `1 <= intervals.length <= 1000`
* `intervals[i].length == 2`
* `0 <= start <= end <= 1000`
---
## Complexity Analysis
* **Time Complexity:**  $\mathcal{O}(N \log N)$ where $N$ is the number of intervals. Sorting the array takes $\mathcal{O}(N \log N)$ time, and merging requires a single $\mathcal{O}(N)$ linear pass.
* **Space Complexity:** $\mathcal{O}(N)$ or $\mathcal{O}(\log N)$ depending on the underlying sorting algorithm's space requirements, plus the $\mathcal{O}(N)$ space required to store the output array of merged intervals.
---
## 🧪 Running the Tests

To run the tests for this specific problem, execute the following command in your terminal from the root directory:
```bash
`pytest test_solution.py -v`
```