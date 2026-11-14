# Trapping Rain Water

## Problem Statement
You are given an array of non-negative integers `height` which represent an elevation map. Each value `height[i]` represents the height of a bar, which has a width of `1`.
Return the maximum area of water that can be trapped between the bars.
---
### Constraints:
* `1 <= height.length <= 1000`
* `0 <= height[i] <= 1000`

---

## Approach: Two Pointers
A brute-force approach would check every bar to see the maximum height to its left and its right, leading to an `O(n^2)` time complexity. We can optimize this to `O(n)` using the **Two-Pointer technique**, eliminating the need for extra arrays (like in dynamic programming) and keeping space complexity strictly `O(1)`.
---
### How it works:
1. Initialize two pointers: `left` at `0` and `right` at `n-1`.
2. Maintain two variables: `max_left` (tallest bar seen from the left) and `max_right` (tallest bar seen from the right). Initialize them with `height[left]` and `height[right]`.
3. While `left < right`:
   * If `max_left < max_right`: The water trapped at the `left` pointer is determined *strictly* by `max_left`. We increment `left`, update `max_left`, and add `max_left - height[left]` to our total water.
   * If `max_right <= max_left`: The water trapped at the `right` pointer is determined *strictly* by `max_right`. We decrement `right`, update `max_right`, and add `max_right - height[right]` to our total.
4. Continue until the pointers cross.
---
### Complexity
* **Time Complexity:** `O(n)` — We traverse the height array only once.
* **Space Complexity:** `O(1)` — Only independent variables are used for state tracking.
---
## How to Run Tests
Ensure both `solution.py` and `test_solution.py` are in the same directory.
Run the tests using the following command in your terminal:
```bash
python3 -m unittest test_solution.py
```