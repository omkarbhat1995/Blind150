# Two Integer Sum II

## Problem Description
Given a 1-indexed array of integers `numbers` that is already sorted in non-decreasing order, find two numbers such that they add up to a specific `target` number. 

Return the indices of the two numbers, `[index1, index2]`, where $1 \le index1 < index2 \le numbers.length$.
---
**Constraints:**
* The solution must use $O(1)$ additional space.
* You may not use the same element twice.
* There will always be exactly one valid solution.
* $2 \le numbers.length \le 1000$
* $-1000 \le numbers[i] \le 1000$
* $-1000 \le target \le 1000$
---
## Solution Approach: Two-Pointer Technique
Because the input array is already sorted, we can solve this problem efficiently using two pointers:
1. Initialize a `left` pointer at the start of the array and a `right` pointer at the end.
2. Calculate the sum of the elements at these two pointers.
3. If the sum equals the target, we have found our pair. (Add 1 to the indices before returning to account for 1-indexing).
4. If the sum is less than the target, we increment the `left` pointer to increase the sum.
5. If the sum is greater than the target, we decrement the `right` pointer to decrease the sum.
---
### Complexity
* **Time Complexity:** $O(n)$ where $n$ is the length of the array. The array is traversed at most once.
* **Space Complexity:** $O(1)$ since only two integer variables are used for the pointers.
---
## How to Run the Tests
This project includes a test suite using Python's built-in `unittest` framework.

1. Ensure you have Python installed on your system.
2. Save the testing script as `test_solution.py`.
3. Run the test file from your terminal:
   `pytest 2-Two-Pointers/test_solution.py -v`
   python -m unittest test_solution.py