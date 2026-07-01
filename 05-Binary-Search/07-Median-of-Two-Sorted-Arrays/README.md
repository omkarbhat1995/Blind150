# Median of Two Sorted Arrays

This project contains the optimal $O(\log(\min(m,n)))$ solution to the "Median of Two Sorted Arrays" problem.

## Problem Description
Given two integer arrays `nums1` and `nums2` of size `m` and `n` respectively, where each is sorted in ascending order, return the median value among all elements of the two arrays.

**Constraints:**
- The overall run time complexity must be $O(\log(m+n))$.

## Approach
To achieve a logarithmic time complexity, we use **Binary Search**.
Instead of merging the two arrays (which would take $O(m+n)$ time), we partition both arrays into two halves such that:
1. The left half contains the exact same number of elements as the right half (or one more if the total number of elements is odd).
2. Every element in the left half is less than or equal to every element in the right half.

By always performing binary search on the **smaller** of the two arrays, we ensure a time complexity of $O(\log(\min(m, n)))$, which satisfies the $O(\log(m+n))$ requirement.

## Complexity
- **Time Complexity**: $O(\log(\min(m, n)))$, because binary search is executed on the smaller array.
- **Space Complexity**: $O(1)$, as we only use a few pointer variables.

## Files
- `solution.py`: Contains the `Solution` class with the implementation.
- `test_median.py`: Contains 16 unit tests covering various edge cases using Python's `unittest` framework.
- `README.md`: This documentation.

## Running Tests
Run the following command in your terminal to execute the test suite:
`python -m unittest test_median.py`