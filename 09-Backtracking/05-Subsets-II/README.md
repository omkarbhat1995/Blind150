# Subsets II

**Difficulty:** Medium
**Category:** Backtracking

## Problem Description
Given an integer array `nums` that may contain duplicates, return all possible subsets (the power set).

The solution set **must not** contain duplicate subsets. Return the solution in any order.
---
**Example 1:**
```text
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
```

**Example 2:**
```text
Input: nums = [0]
Output: [[],[0]]
```
---
**Constraints:**
* `1 <= nums.length <= 11`
* `-20 <= nums[i] <= 20`
---
## Complexity Analysis
* **Time Complexity:** $\mathcal{O}(N \cdot 2^N)$ where $N$ is the length of `nums`. Sorting the array takes $\mathcal{O}(N \log N)$, and there are at most $2^N$ possible subsets. For each subset, it takes up to $\mathcal{O}(N)$ time to copy the elements into the result list.
* **Space Complexity:** $\mathcal{O}(N)$ strictly for the recursion stack and the current subset list being maintained during the backtracking traversal. The output array requires $\mathcal{O}(N \cdot 2^N)$ space, which is typically excluded from auxiliary space analysis.
---