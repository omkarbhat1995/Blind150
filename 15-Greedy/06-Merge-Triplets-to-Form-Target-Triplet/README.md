# Merge Triplets to Form Target

**Difficulty:** Medium
**Category:** Greedy / Arrays

## Problem Description
You are given a 2D array of integers `triplets`, where `triplets[i] = [ai, bi, ci]` represents the `ith` triplet. You are also given an array of integers `target = [x, y, z]` which is the triplet we want to obtain.

To obtain `target`, you may apply the following operation on `triplets` zero or more times:
Choose two different triplets `triplets[i]` and `triplets[j]` and update `triplets[j]` to become `[max(ai, aj), max(bi, bj), max(ci, cj)]`.

Return `true` if it is possible to obtain `target` as an element of `triplets`, or `false` otherwise.
---
**Example 1:**
```text
Input: triplets = [[1,2,3],[7,1,1]], target = [7,2,3]
Output: true
Explanation: Choose the first and second triplets, update the second triplet to be [max(1,7), max(2,1), max(3,1)] = [7,2,3].
```
**Example 2:**
```text
Input: triplets = [[2,5,6],[1,4,4],[5,7,5]], target = [5,4,6]
Output: false
Explanation: It is impossible to obtain [5,4,6] since any triplet that has a 5 in the first position (like [5,7,5]) has an element strictly greater than the target in another position (7 > 4), making it unusable.
```
---
**Constraints:**
* `1 <= triplets.length <= 1000`
* `1 <= ai, bi, ci, x, y, z <= 100`
---
## Complexity Analysis
* **Time Complexity:** $\mathcal{O}(N)$ where $N$ is the number of triplets. The algorithm filters and evaluates each triplet in a single pass.
* **Space Complexity:** $\mathcal{O}(1)$ as we only maintain three boolean flags to track the presence of the required target values across valid triplets.

---
## 🧪 Running the Tests

To run the tests for this specific problem, execute the following command in your terminal from the root directory:
```bash
`pytest test_solution.py -v`
```
