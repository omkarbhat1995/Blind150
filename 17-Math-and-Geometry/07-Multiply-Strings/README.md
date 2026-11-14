# Multiply Strings

This repository contains a Python solution for the [Multiply Strings problem (LeetCode #43)](https://leetcode.com/problems/multiply-strings/).

## Problem Statement

You are given two strings `num1` and `num2` that represent non-negative integers. Return the product of `num1` and `num2` in the form of a string.
---
**Constraints:**
- You cannot use any built-in library to convert the inputs directly into integers (e.g., `int(num1) * int(num2)`).
- `num1` and `num2` consist of digits only.
- `1 <= num1.length, num2.length <= 200`
- Neither `num1` nor `num2` contain leading zeros, unless they are the number "0" itself.
---
## Approach

The solution simulates the manual, paper-and-pencil multiplication process:
1. Initialize an array `res` of size `len(num1) + len(num2)` with zeros. The product of two numbers of length `m` and `n` can never exceed `m + n` digits.
2. Iterate backward through both strings.
3. For each pair of digits at `num1[i]` and `num2[j]`, multiply them.
4. Add the product to the value already present at `res[i + j + 1]`.
5. Update `res[i + j + 1]` with the remainder (modulo 10) and add the carry to `res[i + j]`.
6. Skip any leading zeros in the result array and convert it to a string.
---
# Complexity Analysis
**Time Complexity:** O(M * N) where M and N are the lengths of `num1` and `num2`.
**Space Complexity:** O(M + N) for the result array.
---
## Files
- `solution.py`: Contains the `Solution` class with the `multiply` method.
- `test_solution.py`: Uses the `unittest` framework to test 15 different scenarios, including edge cases.
---
## Running Tests

To run the unit tests, ensure Python is installed and run the following command in the terminal:

```bash
python -m unittest test_solution.py
```
