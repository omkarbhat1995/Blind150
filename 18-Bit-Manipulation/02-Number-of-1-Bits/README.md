# Number of 1 Bits (Hamming Weight)

**Difficulty:** Easy
**Category:** Bit Manipulation

## Problem Description
You are given an unsigned integer `n`. Return the number of `1` bits in its binary representation (also known as the Hamming weight). 

You may assume `n` is a non-negative integer which fits within 32-bits.
---
## Approach
While you can solve this by shifting the bits of `n` to the right 32 times and checking if the lowest bit is a `1` using `n % 2` or `n & 1`, there is a more optimal bit manipulation trick.

We can use the operation `n &= (n - 1)`. 
* Subtracting `1` from a binary number flips all the bits up to and including the lowest set `1` bit.
* Performing a bitwise AND (`&`) between `n` and `n - 1` will effectively clear (set to `0`) the lowest set `1` bit in `n`.
* By repeating this operation in a loop until `n` becomes `0`, we only iterate exactly as many times as there are `1` bits in the number.
---
## Complexity  Analysis
* **Time Complexity:** O(1) - In the worst-case scenario (all 1s), the loop runs 32 times. Since 32 is a constant bounded by the 32-bit integer constraint, the time complexity is constant.
* **Space Complexity:** O(1) - We only use a single variable to keep track of the count, requiring no extra scaling memory.
---
## 🧪 Running the Tests

To run the tests for this specific problem, execute the following command in your terminal from the root directory:
```bash
`pytest 01-Arrays-and-Hashing/07-Product-of-Array-Except-Self/test_solution.py -v`
```