# Find the Duplicate Number

**Difficulty:** Medium
**Topics:** Array, Two Pointers, Binary Search, Bit Manipulation

## Problem Description

You are given an array of integers `nums` containing `n + 1` integers. Each integer in `nums` is in the range `[1, n]` inclusive.

There is exactly one repeated integer in `nums`, and every other integer appears at most once.

Return the repeated integer.

**Follow-up:** Can you solve the problem without modifying the array `nums` and using $O(1)$ extra space?

## Approach: Floyd's Tortoise and Hare (Cycle Detection)

Because the numbers in the array are bounded between `1` and `n`, and the array size is `n + 1`, we can treat the array as a linked list. The value at a given index points to the next index (i.e., `next_node = nums[current_index]`). 

Since there are multiple pointers pointing to the same index (the duplicate number), a cycle is mathematically guaranteed to exist.

1. **Phase 1 (Find Intersection):** We use a slow pointer (moves 1 step) and a fast pointer (moves 2 steps). They will eventually meet inside the cycle.
2. **Phase 2 (Find Entrance):** Once they meet, we move a third pointer from the start of the array and the slow pointer from the intersection point, both moving 1 step at a time. The point where they collide is the entrance to the cycle, which is our duplicate number.

## Complexity
- **Time Complexity:** $O(n)$ where `n` is the length of the array. We traverse the array a constant number of times.
- **Space Complexity:** $O(1)$. We only use