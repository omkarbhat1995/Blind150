# Sum of Two Integers

**Difficulty:** Medium
**Category:** Bit Manipulation

## Problem Description
Given two integers `a` and `b`, return the sum of the two integers without using the `+` and `-` operators.
---
## Approach
To add two numbers without standard arithmetic operators, we must simulate addition at the bit level using logic gates (Bitwise operations).

1. **Addition without Carry:** The bitwise XOR (`^`) operator adds two bits together but drops the carry (e.g., `1 ^ 1 = 0`, `1 ^ 0 = 1`).
2. **Calculating the Carry:** The bitwise AND (`&`) operator identifies positions where both bits are `1` (which generates a carry). We then shift this result left by 1 (`<< 1`) to carry it over to the next bit position.
3. We repeat this process until there is no carry left (`b == 0`).

**Python Specifics:**
Unlike languages like Java or C++ which use fixed 32-bit integers, Python handles integers with arbitrary precision (infinite bits). This means negative numbers have an infinite number of leading `1`s in binary. To simulate the 32-bit overflow expected in this problem, we must manually mask the integers to 32 bits using `0xFFFFFFFF`. Finally, if the result is negative in a 32-bit context, we convert it back to Python's standard representation using two's complement.
---
## Complexity  Analysis
* **Time Complexity:** $O(1)$ - In a 32-bit integer system, the loop runs at most 32 times, which is constant.
* **Space Complexity:** $O(1)$ - Only constant extra space is used.
---
## 🧪 Running the Tests

To run the tests for this specific problem, execute the following command in your terminal from the root directory:
```bash
`pytest 01-Arrays-and-Hashing/07-Product-of-Array-Except-Self/test_solution.py -v`
```