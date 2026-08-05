# Pow(x, n)

## Problem Description
Implement a mathematical function to calculate the value of `x` raised to the power of `n` (i.e., `x^n`). 

Given a floating-point value `x` and an integer value `n`, implement the `myPow(x, n)` function without using any built-in library functions.

## Examples
**Example 1:**
- **Input:** `x = 2.00000, n = 5`
- **Output:** `32.00000`

**Example 2:**
- **Input:** `x = 1.10000, n = 10`
- **Output:** `2.59374`

**Example 3:**
- **Input:** `x = 2.00000, n = -3`
- **Output:** `0.12500`

## Constraints
- `-100.0 < x < 100.0`
- `-1000 <= n <= 1000`
- `n` is an integer.
- If `x = 0`, then `n` will be positive.

## Approach & Complexity
This solution utilizes **Binary Exponentiation** (Exponentiation by Squaring) to significantly reduce the number of multiplications. Instead of multiplying `x` by itself `n` times, we square the base and halve the exponent iteratively. If the exponent is odd, we multiply the current result by the base before halving. For negative exponents, we simply invert the base `x` and convert `n` to a positive integer.

- **Time Complexity:** $O(\log n)$ because we halve the exponent `n` on each iteration.
- **Space Complexity:** $O(1)$ as we only use a few variables to maintain the running state without utilizing the recursive call stack.