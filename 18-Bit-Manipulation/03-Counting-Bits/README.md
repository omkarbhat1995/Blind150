# Counting Bits

**Difficulty:** Easy
**Category:** Dynamic Programming / Bit Manipulation

## Problem Description
Given an integer `n`, count the number of `1`'s in the binary representation of every number in the range `[0, n]`.

Return an array `output` where `output[i]` is the number of `1`'s in the binary representation of `i`.
---
## Approach
While we could calculate the Hamming weight for each number individually using a loop, we can achieve an optimal linear time solution by looking for a pattern using **Dynamic Programming**.

When you shift a binary number to the right by 1 (which is equivalent to integer division by 2):
* `4` in binary is `100`. Shifted right, it becomes `10` (which is `2`).
* `5` in binary is `101`. Shifted right, it becomes `10` (which is `2`).

Notice that:
* The number of `1`s in an even number (like `4`) is the exact same as the number of `1`s in its half (`2`). This is because multiplying by 2 just adds a `0` to the end of the binary string.
* The number of `1`s in an odd number (like `5`) is the number of `1`s in its half (`2`) **plus one**. This is because the lowest bit of an odd number is always `1`.

We can express this relation as:
`dp[i] = dp[i >> 1] + (i & 1)`
Where `i >> 1` divides `i` by 2, and `i & 1` checks if `i` is odd (returns `1` if odd, `0` if even).
---
## Complexity  Analysis
* **Time Complexity:** O(n) - We calculate the bits for each number from `1` to `n` in exactly one pass, doing O(1) work per number.
* **Space Complexity:** O(n) - We allocate an array of size `n + 1` to store and return the result.
---
## 🧪 Running the Tests

To run the tests for this specific problem, execute the following command in your terminal from the root directory:
```bash
`pytest 01-Arrays-and-Hashing/07-Product-of-Array-Except-Self/test_solution.py -v`
```