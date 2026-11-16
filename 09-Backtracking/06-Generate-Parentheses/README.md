# Generate Parentheses

**Difficulty:** Medium
**Category:** Backtracking / Stack

## Problem Description
You are given an integer `n`. Return all well-formed parentheses strings that you can generate with `n` pairs of parentheses.

You may return the answer in any order.
---
**Example 1:**
```text
Input: n = 1
Output: ["()"]
```
**Example 2:**
```text
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
```
---
**Constraints:**
* `1 <= n <= 7`
---

## Complexity Analysis
* **Time Complexity:** $\mathcal{O}\left(\frac{4^n}{\sqrt{n}}\right)$ because the algorithm explores valid sequences matching the $n$-th Catalan number. Backtracking guarantees we only build well-formed paths, skipping invalid permutations entirely.
* **Space Complexity:** $\mathcal{O}(n)$ to store the recursion call stack and the current path array of length $2n$. (Space allocated for the final output array is excluded from auxiliary space analysis).

---
## 🧪 Running the Tests

To run the tests for this specific problem, execute the following command in your terminal from the root directory:
```bash
`pytest test_solution.py -v`
```