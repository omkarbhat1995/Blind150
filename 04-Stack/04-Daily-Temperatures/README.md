# Daily Temperatures

## Problem Description
You are given an array of integers `temperatures` where `temperatures[i]` represents the daily temperatures on the `ith` day.

Return an array `result` where `result[i]` is the number of days after the `ith` day before a warmer temperature appears on a future day. If there is no day in the future where a warmer temperature will appear for the `ith` day, set `result[i]` to `0` instead.

**Constraints:**
- `1 <= temperatures.length <= 1000`
- `1 <= temperatures[i] <= 100`

## Approach: Monotonic Decreasing Stack
A brute-force solution would check every future day for every single day, resulting in a slow O(n^2) time complexity. We can optimize this to O(n) by using a **Monotonic Decreasing Stack**.

1. We initialize an array `res` of the same length as `temperatures`, filled with `0`s.
2. We iterate through the `temperatures` array, maintaining a stack that stores pairs of `[temperature, index]`.
3. The stack is kept strictly **decreasing**. If we encounter a temperature that is *warmer* than the temperature at the top of the stack, we know we have found the "next warmer day" for that top element.
4. We pop the element from the stack, calculate the difference in indices (`current_index - popped_index`), and store this distance in our `res` array.
5. We continue popping until the stack is empty or the current temperature is no longer warmer than the top of the stack, then push the current `[temperature, index]` pair.

## Complexity
- **Time Complexity:** O(n) - We iterate through the array once, and each element is pushed and popped from the stack at most once.
- **Space Complexity:** O(n) - In the worst-case scenario (e.g., strictly decreasing temperatures), the stack will grow to the size of the array.