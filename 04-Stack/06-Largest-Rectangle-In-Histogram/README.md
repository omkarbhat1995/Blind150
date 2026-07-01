# Largest Rectangle In Histogram

## Problem Description
You are given an array of integers `heights` where `heights[i]` represents the height of a bar. The width of each bar is `1`.

Return the area of the largest rectangle that can be formed among the bars.

**Constraints:**
- `1 <= heights.length <= 1000`
- `0 <= heights[i] <= 1000`

## Approach: Monotonic Stack
A brute-force solution would expand outward from every bar to find the maximum width it can sustain, taking O(n²) time. We can optimize this to O(n) using a **Monotonic Stack**.

1. We use a stack to store pairs of `(index, height)`. We want to maintain a strictly increasing stack of heights.
2. We iterate through the `heights` array. 
3. If the current height is *less* than the height at the top of the stack, it means the rectangle for the stack's top height cannot be extended any further to the right. 
4. We continuously pop elements from the stack as long as this condition holds. For each popped element, we calculate the area: `height * (current_index - popped_index)`. We update our maximum area.
5. Crucially, when we push the new, shorter height onto the stack, we push it with the **index of the furthest element we just popped**. This is because the new height could theoretically stretch all the way back through those taller bars.
6. Once the loop finishes, any remaining elements in the stack can extend all the way to the end of the histogram. We pop them and calculate their areas using the total length of the array.

## Complexity
- **Time Complexity:** O(n) - We iterate through the array once, and each bar is pushed and popped from the stack at most once.
- **Space Complexity:** O(n) - In the worst-case scenario (e.g., strictly increasing heights), the stack will grow proportionally to the number of bars.