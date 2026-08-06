# Missing Number

**Difficulty:** Easy
**Category:** Arrays & Hashing / Math

## Problem Description
Given an array `nums` containing `n` integers in the range `[0, n]` without any duplicates, return the single number in the range that is missing from `nums`.

## Approach
To achieve $O(n)$ runtime and $O(1)$ space complexity, we can use a mathematical approach based on **Gauss's Formula**.

The sum of the first `n` numbers (from `0` to `n`) can be calculated directly using the formula:
`Expected Sum = n * (n + 1) / 2`

Because the input array contains exactly `n` numbers and is missing exactly one number in that sequence, we can:
1. Calculate the expected sum of the complete sequence `[0, n]`.
2. Calculate the actual sum of the elements currently in the `nums` array.
3. Subtract the actual sum from the expected sum. The difference is the missing number.

*Note: In languages like C++ or Java, adding a large sequence of numbers can cause integer overflow. In those cases, a Bit Manipulation (XOR) approach is often preferred. However, Python handles arbitrarily large integers automatically, making this mathematical approach perfectly safe and extremely fast.*

## Complexity
* **Time Complexity:** $O(n)$ - We iterate through the array exactly once to calculate the sum.
* **Space Complexity:** $O(1)$ - We only use a few variables to store our sums.