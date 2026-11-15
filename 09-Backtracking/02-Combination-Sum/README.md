# Combination Sum

**Difficulty:** Medium
**Category:** Backtracking

## Problem Description
Given an array of distinct integers `nums` and a target integer `target`, return a list of all unique combinations of `nums` where the chosen numbers sum to `target`.

The same number may be chosen from `nums` an unlimited number of times. Two combinations are the same if the frequency of each of the chosen numbers is the same.

**Example 1:**
\`\`\`text
Input: nums = [2,5,6,9], target = 9
Output: [[2,2,5],[9]]
Explanation:
2 + 2 + 5 = 9. We use 2 twice, and 5 once.
9 = 9. We use 9 once.
\`\`\`

**Constraints:**
* `1 <= nums.length <= 20`
* `2 <= nums[i] <= 30`
* `2 <= target <= 30`
* All elements of `nums` are distinct.

## Complexity Analysis
* **Time Complexity:** $\mathcal{O}(2^{\frac{T}{M}})$ where $T$ is the target value and $M$ is the minimum value in the `nums` array. In the worst case, the algorithm explores a decision tree where the maximum depth is $\frac{T}{M}$.
* **Space Complexity:** $\mathcal{O}(\frac{T}{M})$ strictly for the recursion stack space and the current combination list being maintained.

## 🧪 Running the Tests

To run the tests for this specific problem, execute the following command in your terminal from the root directory:
```bash
`pytest test_solution.py -v`
```