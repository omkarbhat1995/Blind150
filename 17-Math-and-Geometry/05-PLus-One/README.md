# Plus One

## Problem Description
You are given an integer array `digits`, where each `digits[i]` is the `i`th digit of a large integer. It is ordered from most significant to least significant digit, and it will not contain any leading zero.

Return the digits of the given integer after incrementing it by one.
---
## Examples
**Example 1:**
- **Input:** `digits = [1,2,3,4]`
- **Output:** `[1,2,3,5]`
- **Explanation:** 1234 + 1 = 1235.

**Example 2:**
- **Input:** `digits = [9,9,9]`
- **Output:** `[1,0,0,0]`
- **Explanation:** 999 + 1 = 1000.
---
## Constraints
- `1 <= digits.length <= 100`
- `0 <= digits[i] <= 9`
- `digits` does not contain any leading zeros.
---
## Approach & Complexity
This solution iterates through the array in reverse (from the least significant digit to the most). If a digit is less than 9, we simply increment it by 1 and return the array immediately. If it is 9, it becomes 0, and the loop continues to handle the carry. If the loop completes without returning, it means all digits were 9s. In this case, we simply prepend a `1` to the array.

## Complexity  Analysis
- **Time Complexity:** **O(n)** where n is the number of digits. In the worst case, we traverse the entire array.
- **Space Complexity:** **O(1)** in-place modification for most cases. Worst-case (all 9s) requires **O(n)** space to return a new expanded array.

---

## 🧪 Running the Tests

To run the tests for this specific problem, execute the following command in your terminal from the root directory:
```bash
`pytest 01-Arrays-and-Hashing/07-Product-of-Array-Except-Self/test_solution.py -v`
```