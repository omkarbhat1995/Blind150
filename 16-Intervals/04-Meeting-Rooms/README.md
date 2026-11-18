# Meeting Rooms

**Difficulty:** Easy
**Category:** Arrays / Sorting

## Problem Description
Given an array of meeting time interval objects consisting of start and end times `[[start_1,end_1],[start_2,end_2],...]` (`start_i < end_i`), determine if a person could add all meetings to their schedule without any conflicts. The intervals may be provided in any order.

*Note: `(0,8),(8,10)` is not considered a conflict at 8.*
---
**Example 1:**
```text
Input: intervals = [(0,30),(5,10),(15,20)]
Output: false
Explanation:
(0,30) and (5,10) will conflict
(0,30) and (15,20) will conflict
```
**Example 2:**
```text
Input: intervals = [(5,8),(9,15)]
Output: true
```
---
**Constraints:**
* `0 <= intervals.length <= 500`
* `0 <= intervals[i].start < intervals[i].end <= 1,000,000`
---
## Complexity Analysis
* **Time Complexity:** $\mathcal{O}(N \log N)$ where $N$ is the number of meetings. Sorting the array of intervals takes $\mathcal{O}(N \log N)$ time, and the subsequent linear scan takes $\mathcal{O}(N)$ time.
* **Space Complexity:** $\mathcal{O}(1)$ or $\mathcal{O}(N)$ depending on the sorting algorithm implementation in the language (Python's Timsort takes $\mathcal{O}(N)$ space in the worst case).
---
## 🧪 Running the Tests

To run the tests for this specific problem, execute the following command in your terminal from the root directory:
```bash
`pytest test_solution.py -v`
```