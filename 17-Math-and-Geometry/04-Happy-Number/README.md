# Non-Cyclical Number

## Problem Description
A non-cyclical number is an integer defined by the following algorithm:
1. Given a positive integer, replace it with the sum of the squares of its digits.
2. Repeat the above step until the number equals 1, or it loops infinitely in a cycle which does not include 1.
3. If it stops at 1, then the number is a non-cyclical number.

Given a positive integer `n`, return `true` if it is a non-cyclical number, otherwise return `false`.
---
## Examples
**Example 1:**
- **Input:** `n = 100`
- **Output:** `true`
- **Explanation:** - $1^2 + 0^2 + 0^2 = 1$

**Example 2:**
- **Input:** `n = 101`
- **Output:** `false`
- **Explanation:** - $1^2 + 0^2 + 1^2 = 2$
  - $2^2 = 4$
  - $4^2 = 16$
  - $1^2 + 6^2 = 37$
  - $3^2 + 7^2 = 58$
  - $5^2 + 8^2 = 89$
  - $8^2 + 9^2 = 145$
  - $1^2 + 4^2 + 5^2 = 42$
  - $4^2 + 2^2 = 20$
  - $2^2 + 0^2 = 4$ (Cycle detected)
---
## Constraints
- `1 <= n <= 1000`
---
## Approach & Complexity
This solution uses **Floyd's Cycle Detection Algorithm** (Fast and Slow pointers) to find cycles without using additional memory. We calculate the sum of the squares of the digits for a "slow" pointer moving one step at a time, and a "fast" pointer moving two steps at a time. If they meet at 1, the number is non-cyclical. If they meet at any other number, a cycle exists.

## Complexity Analysis
- **Time Complexity:** $O(\log n)$ to calculate the digit square sums.
- **Space Complexity:** $O(1)$ since we only use two integer pointers instead of a dynamically growing Hash Set.

---

## 🧪 Running the Tests

To run the tests for this specific problem, execute the following command in your terminal from the root directory:
```bash
`pytest 01-Arrays-and-Hashing/07-Product-of-Array-Except-Self/test_solution.py -v`
```