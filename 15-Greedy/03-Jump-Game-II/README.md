# Jump Game II

**Difficulty:** Medium
**Category:** Greedy / Array

## Problem Description
You are given an array of integers `nums`, where `nums[i]` represents the maximum length of a jump towards the right from index `i`. 

You are initially positioned at `nums[0]`. Return the **minimum** number of jumps to reach the last position in the array (index `nums.length - 1`). You may assume there is always a valid answer.
---
**Example 1:**
```text
Input: nums = [2,4,1,1,1,1]
Output: 2
Explanation: Jump from index 0 to index 1, then jump from index 1 to the last index.
```
**Example 2:**
```text
Input: nums = [2,1,2,1,0]
Output: 2
```
**Constraints:** 
* `1 <= nums.length <= 1000`
* `0 <= nums[i] <= 100`
---
## Complexity Analysis
* **Time Complexity:**  $\mathcal{O}(N)$ where $N$ is the length of the array. We iterate through the array once using a sliding window approach.
* **Space Complexity:** $\mathcal{O}(1)$ because we only maintain a few integer variables (jumps, left, right, and farthest) to track our BFS-style bounds, regardless of the input size.

---
## 🧪 Running the Tests

To run the tests for this specific problem, execute the following command in your terminal from the root directory:
```bash
`pytest test_solution.py -v`
```