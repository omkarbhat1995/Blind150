# Reverse Integer

**Difficulty:** Medium
**Category:** Math

## Problem Description
You are given a signed 32-bit integer `x`.

Return `x` after reversing each of its digits. After reversing, if `x` goes outside the signed 32-bit integer range $[-2^{31}, 2^{31} - 1]$, then return `0` instead.

**Constraint:** Solve the problem without using integers that are outside the signed 32-bit integer range.

## Approach
To reverse an integer mathematically without converting it to a string, we can repeatedly "pop" the last digit off the input number and "push" it onto the back of our result variable.

1. **Pop:** Extract the last digit using the modulo operator (`x % 10`) and reduce the input size using integer division (`x // 10`).
2. **Push:** Multiply the running result by 10 and add the popped digit (`res = res * 10 + pop`).
3. **Overflow Check:** Because we are strictly bound by the 32-bit integer limits ($-2147483648$ to $2147483647$), we must check if our `res` will overflow *before* we multiply it by 10. 
   * If `res > 214748364`, multiplying by 10 will definitely overflow.
   * If `res == 214748364`, multiplying by 10 gives `2147483640`. Adding a `pop` digit greater than `7` will overflow. 

*(Note: In Python, `%` and `//` handle negative numbers differently than C++/Java. To simplify, we can work with the absolute value of `x` and apply the negative sign at the very end.)*

## Complexity
* **Time Complexity:** $O(\log_{10}(x))$ - The number of digits in $x$ determines the number of iterations. Since $x$ is a 32-bit integer, it has at most 10 digits, making this effectively $O(1)$ constant time.
* **Space Complexity:** $O(1)$ - We only use a few variables for the calculation.