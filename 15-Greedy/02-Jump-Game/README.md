# Jump Game

**Difficulty:** Medium
**Category:** Greedy / Array

## Problem Description
You are given an integer array `nums` where each element `nums[i]` indicates your maximum jump length at that position.

Return `true` if you can reach the last index starting from index 0, or `false` otherwise.

**Example 1:**
```text
Input: nums = [1,2,0,1,0]
Output: true
Explanation: First jump from index 0 to 1, then from index 1 to 3, and lastly from index 3 to 4.
```

**Example 2:**
```text
Input: nums = [1,2,1,0,1]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
```

**Constraints:**
* `1 <= nums.length <= 1000` 
* `0 <= nums[i] <= 1000`

## Complexity Analysis
* **Time Complexity:** $\mathcal{O}(n)$ where $n$ is the length of the array. We perform a single backward pass through the array.
* **Space Complexity:** $\mathcal{O}(1)$ because the algorithm only requires a single integer variable (goal) to track the shifting target state.

---
## 🧪 Running the Tests

To run the tests for this specific problem, execute the following command in your terminal from the root directory:
```bash
`pytest test_solution.py -v`
```