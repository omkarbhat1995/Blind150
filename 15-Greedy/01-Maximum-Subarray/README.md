# Maximum Subarray

**Difficulty:** Medium
**Category:** Arrays / Dynamic Programming (Kadane's Algorithm)

## Problem Description
Given an array of integers `nums`, find the subarray (a contiguous non-empty sequence of elements) with the largest sum and return the sum.
---
**Example 1:**
```text
Input: nums = [2,-3,4,-2,2,1,-1,4]
Output: 8
Explanation: The subarray [4,-2,2,1,-1,4] has the largest sum 8.
```
**Example 2:**
```text
Input: nums = [-1]
Output: -1
```
---
**Constraints:**

* `1 <= nums.length <= 100,000`
* `-10,000 <= nums[i] <= 10,000`

---
## Complexity Analysis
* **Time Complexity:** $\mathcal{O}(N)$ where $N$ is the number of elements in the array. We iterate through the array exactly once, making it a highly optimal single-pass solution.
* **Space Complexity:** $\mathcal{O}(1)$ because we only use two variables (current_sum and max_sum) to track our running totals, requiring no auxiliary data structures.

---
## 🧪 Running the Tests

To run the tests for this specific problem, execute the following command in your terminal from the root directory:
```bash
`pytest test_solution.py -v`
```