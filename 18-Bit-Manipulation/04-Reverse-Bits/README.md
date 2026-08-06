# Reverse Bits

**Difficulty:** Easy
**Category:** Bit Manipulation

## Problem Description
Given a 32-bit unsigned integer `n`, reverse the bits of the binary representation of `n` and return the result.

## Approach
To reverse the bits of a 32-bit integer, we can process the number bit by bit, from the least significant bit (LSB) to the most significant bit (MSB).

1. Initialize a result variable `res` to `0`.
2. Loop exactly 32 times (since the problem guarantees a 32-bit integer):
   * Extract the rightmost bit of `n` using bitwise AND (`n & 1`).
   * Shift the `res` to the left by 1 position (`res << 1`) to make room for the new bit.
   * Add the extracted bit to `res` using bitwise OR (`res | bit`).
   * Shift `n` to the right by 1 position (`n >> 1`) to process the next bit in the sequence.
3. Return the fully constructed `res`.

## Complexity
* **Time Complexity:** $O(1)$ - The loop always runs exactly 32 times regardless of the input size, meaning it executes in constant time.
* **Space Complexity:** $O(1)$ - We only use a single variable (`res`) to store the reversed integer.