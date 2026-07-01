# Sliding Window Maximum

**Difficulty:** Hard
**Category:** Sliding Window / Queues

## Problem Description

You are given an array of integers `nums` and an integer `k`. There is a sliding window of size `k` that starts at the left edge of the array. The window slides one position to the right until it reaches the right edge of the array.

Return a list that contains the maximum element in the window at each step.

### Examples

**Example 1:**
- **Input:** `nums = [1, 2, 1, 0, 4, 2, 6], k = 3`
- **Output:** `[2, 2, 4, 4, 6]`
- **Explanation:**
  - Window `[1, 2, 1]` -> Max: 2
  - Window `[2, 1, 0]` -> Max: 2
  - Window `[1, 0, 4]` -> Max: 4
  - Window `[0, 4, 2]` -> Max: 4
  - Window `[4, 2, 6]` -> Max: 6

**Example 2:**
- **Input:** `nums = [1], k = 1`
- **Output:** `[1]`

### Constraints
- `1 <= nums.length <= 100000`
- `-10000 <= nums[i] <= 10000`
- `1 <= k <= nums.length`

## Optimal Approach

The optimal solution uses a **Monotonically Decreasing Deque** (Double-Ended Queue). Instead of scanning the window to find the maximum every time it shifts, we store the *indices* of the elements in the deque in such a way that the values corresponding to those indices are strictly decreasing. 

1. As we expand the window, we pop elements from the right of the deque if they are smaller than the current element (because they can never be the maximum of any future window).
2. We remove the leftmost index from the deque if it falls out of the current window's bounds.
3. The maximum for the current window is always at the front (leftmost) of the deque.

### Complexity
- **Time Complexity:** $O(n)$ where $n$ is the length of `nums`. Every element is pushed and popped from the deque at most once.
- **Space Complexity:** $O(k)$ since the deque will store at most $k$ indices at any given time.