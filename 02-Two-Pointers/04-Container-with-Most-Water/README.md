# Container With Most Water

## Problem Statement
You are given an integer array `heights` where `heights[i]` represents the height of the `ith` bar. 
You may choose any two bars to form a container. Return the maximum amount of water a container can store.

### Constraints:
* `2 <= height.length <= 1000`
* `0 <= height[i] <= 1000`

---

## Approach: Two Pointers
A brute-force approach would check every possible pair of bars, resulting in an `O(n^2)` time complexity. However, we can optimize this to `O(n)` using the **Two-Pointer technique**.

### How it works:
1. Initialize two pointers: `left` at the beginning (index 0) and `right` at the end (index `n-1`) of the array.
2. Calculate the area formed by the bars at the `left` and `right` pointers: `Area = min(height[left], height[right]) * (right - left)`.
3. Track the maximum area seen so far.
4. **The Greedy Step:** The height of the water is dictated by the *shorter* bar. Moving the pointer of the taller bar inward cannot possibly increase the height of the water, and it strictly decreases the width, meaning the area will always decrease or stay the same. Therefore, we should always move the pointer pointing to the **shorter bar** inward, hoping to find a taller bar that can make up for the loss in width.
5. Repeat until the `left` and `right` pointers meet.

### Complexity
* **Time Complexity:** `O(n)` — We only pass through the array a single time, as each step moves one pointer closer to the other.
* **Space Complexity:** `O(1)` — We only use a few integer variables (`left`, `right`, `max_water`) to track our state. No auxiliary space is required.

## How to Run Tests
Ensure both `solution.py` and `test_solution.py` are in the same directory.
Run the tests using the following command in your terminal:
```bash
python3 -m unittest test_solution.py
```