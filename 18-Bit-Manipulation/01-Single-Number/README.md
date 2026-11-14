# Single Number

**Difficulty:** Easy
**Category:** Arrays & Hashing / Bit Manipulation

## Problem Description
You are given a non-empty array of integers `nums`. Every integer appears twice except for one.

Return the integer that appears only once.

You must implement a solution with a linear runtime complexity and use only constant extra space.
---
## Approach
To achieve $O(n)$ time complexity and $O(1)$ space complexity, we can use **Bitwise XOR** (`^`). 

The XOR operator has the following mathematical properties:
1. `a ^ 0 = a`
2. `a ^ a = 0`
3. Associativity/Commutativity: `a ^ b ^ a = (a ^ a) ^ b = 0 ^ b = b`

By sequentially XORing all elements in the array together, every number that appears twice will cancel itself out (become `0`), regardless of the order they appear in. The only number left at the end of the loop will be the integer that appears exactly once.
---
## Complexity Analysis
* **Time Complexity:** $O(n)$ - We iterate through the input array exactly once.
* **Space Complexity:** $O(1)$ - We only use a single variable to keep track of the running XOR sum, regardless of the array's size.
---
## 🧪 Running the Tests

To run the tests for this specific problem, execute the following command in your terminal from the root directory:
```bash
`pytest 01-Arrays-and-Hashing/07-Product-of-Array-Except-Self/test_solution.py -v`
```