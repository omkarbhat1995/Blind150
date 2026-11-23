# Climbing Stairs

**Difficulty:** Easy  
**Category:** 1-D Dynamic Programming

## Problem Description
You are given an integer `n` representing the number of steps to reach the top of a staircase. You can climb with either `1` or `2` steps at a time.

Return the number of distinct ways to climb to the top of the staircase.
---
**Example 1:**
```text
Input: n = 2
Output: 2
Explanation:
1 + 1 = 2
2 = 2
```
**Example 2:**
```text
Input: n = 3
Output: 3
Explanation:
1 + 1 + 1 = 3
1 + 2 = 3
2 + 1 = 3
```
---
**Constraints:**
* `1 <= n <= 45`
---
## Complexity Analysis
* **Time Complexity:** $\mathcal{O}(n)$ where $n$ is the number of steps. We compute each step's count once in a single bottom-up pass.   
* **Space Complexity:** $\mathcal{O}(1)$ because we only maintain two variables (one_step_before and two_steps_before) rather than storing a full DP array. 
---  
## 🧪 Running the Tests

To run the tests for this specific problem, execute the following command in your terminal from the root directory:
```bash
`pytest test_solution.py -v`
```