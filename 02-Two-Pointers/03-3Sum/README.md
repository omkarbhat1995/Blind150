# 3Sum Solution

## Problem Description
Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` where `nums[i] + nums[j] + nums[k] == 0`, and the indices `i`, `j` and `k` are all distinct.

The output must not contain any duplicate triplets. 
---
## Solution Approach: Sorting + Two Pointers
Since we need to find triplets that sum to 0, we can sort the array first. Sorting helps us avoid duplicate triplets and allows us to use the efficient two-pointer technique.

1. **Sort the Array:** Time complexity is $O(N \log N)$.
2. **Iterate & Fix one element:** Iterate through the array with an index `i`. This fixes `nums[i]` as the first element of our potential triplet. The goal then becomes finding two other numbers in the array that sum to `-nums[i]`.
3. **Two Pointers:** For each `nums[i]`, set a `left` pointer to `i + 1` and a `right` pointer to the end of the array.
4. **Skip Duplicates:** * If `nums[i] == nums[i-1]`, skip the element to prevent generating duplicate triplets from the start.
    * If a valid triplet is found, advance both `left` and `right` pointers, skipping over any adjacent duplicate values.
---
### Complexity
* **Time Complexity:** $O(N^2)$, where $N$ is the number of elements in the array. The outer loop runs $O(N)$ times, and inside it, the two pointers scan the remaining array in $O(N)$ time.
* **Space Complexity:** $O(1)$ auxiliary space (or $O(N)$ depending on the underlying sorting algorithm).
---
## How to Run the Tests
This directory contains a complete test suite using Python's built-in `unittest` framework.

1. Ensure you have Python installed on your system.
2. Open your terminal and navigate to the directory containing these files.
3. Run the test file:
`pytest 03-3Sum/test_solution.py -v`