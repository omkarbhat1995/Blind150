# Subsets
**Difficulty**: Medium
**Category**: Backtracking

## Problem Description
Given an array nums of unique integers, return all possible subsets (the power set).The solution set must not contain duplicate subsets. Return the solution in any order.
---
**Example 1:**
```text
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
```
```text
**Example 2:**
Input: nums = [7]
Output: [[],[7]]
```
---
**Constraints:**
1 <= nums.length <= 10
-10 <= nums[i] <= 10

All the numbers of nums are unique.

## Complexity Analysis
* **Time Complexity:** $\mathcal{O}(N \times 2^N)$ where $N$ is the length of the input array. There are exactly $2^N$ possible subsets, and for each subset, it takes $\mathcal{O}(N)$ time to copy the current combination into the final result list.
* **Space Complexity:** $\mathcal{O}(N)$ for the recursion stack during the backtracking process. If we count the space needed to hold the output array, it becomes $\mathcal{O}(N \times 2^N)$

## 🧪 Running the Tests

To run the tests for this specific problem, execute the following command in your terminal from the root directory:
```bash
`pytest test_solution.py -v`
```