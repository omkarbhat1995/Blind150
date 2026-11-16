# Permutations

**Difficulty:** Medium
**Category:** Backtracking

## Problem Description
Given an array `nums` of unique integers, return all the possible permutations. You may return the answer in any order.
---
**Example 1:**
```text
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```
**Example 2:**
```text
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Input: nums = [7]
Output: [[7]]
```
---
**Constraints:**
* `1 <= nums.length <= 6`
* `-10 <= nums[i] <= 10`
All the integers of nums are unique

---
## Complexity Analysis
* **Time Complexity:** $\mathcal{O}(N \cdot N!)$ where $N$ is the length of the input array. There are $N!$ possible permutations, and it takes $\mathcal{O}(N)$ time to copy each valid permutation into the result list.
* **Space Complexity:** $\mathcal{O}(N)$ for the recursion stack depth, the path list being maintained during traversal, and the used array tracking active elements. The space used to hold the final output of permutations is generally excluded from auxiliary space analysis.
---
## 🧪 Running the Tests

To run the tests for this specific problem, execute the following command in your terminal from the root directory:
```bash
`pytest test_solution.py -v`
```