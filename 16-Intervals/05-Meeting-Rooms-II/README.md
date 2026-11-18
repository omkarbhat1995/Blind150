# Meeting Rooms II

**Difficulty:** Medium
**Category:** Intervals / Sorting / Two Pointers

## Problem Description
Given an array of meeting time interval objects consisting of start and end times `[[start_1,end_1],[start_2,end_2],...]` (`start_i < end_i`), find the minimum number of rooms required to schedule all meetings without any conflicts.

*Note: `(0,8),(8,10)` is NOT considered a conflict at 8.*
---
**Example 1:**
```text
Input: intervals = [(0,40),(5,10),(15,20)]
Output: 2
Explanation:
room1: (0,40)
room2: (5,10),(15,20)
```
**Example 2:**
```text
Input: intervals = [(4,9)]
Output: 1
```
---
**Constraints:**
* `0 <= intervals.length <= 100,000`
* `0 <= intervals[i].start < intervals[i].end <= 1,000,000`
---
Complexity AnalysisTime Complexity: $\mathcal{O}(N \log N)$ where $N$ is the number of meetings. Extracting and sorting the start and end times independently takes $\mathcal{O}(N \log N)$ time. The two-pointer traversal takes $\mathcal{O}(N)$ time.Space Complexity: $\mathcal{O}(N)$ to store the separated arrays for start and end times.
---
## 🧪 Running the Tests

To run the tests for this specific problem, execute the following command in your terminal from the root directory:
```bash
`pytest test_solution.py -v`
```